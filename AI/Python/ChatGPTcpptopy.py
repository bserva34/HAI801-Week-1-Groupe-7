import heapq

class Node:
    def __init__(self, name, cost):
        self.name = name
        self.cost = cost
        self.neighbors = []
        self.cost_neighbors = []

class Graph:
    def __init__(self):
        self.nodes = []

    def find_index(self, node_name):
        for i, node in enumerate(self.nodes):
            if node.name == node_name:
                return i
        return -1

    def a_star(self, start_node, goal_node):
        open_set = [(0, start_node)]
        g_values = [float('inf')] * len(self.nodes)
        visited = [False] * len(self.nodes)
        parents = [-1] * len(self.nodes)

        start_idx = self.find_index(start_node)
        goal_idx = self.find_index(goal_node)

        if start_idx == -1 or goal_idx == -1:
            print("Invalid start or goal node.")
            return []

        heapq.heappush(open_set, (0, start_idx))
        g_values[start_idx] = 0

        while open_set:
            current_cost, current_idx = heapq.heappop(open_set)

            if current_idx == goal_idx:
                # Reconstruct the path
                node = goal_idx
                path = []
                while node != -1:
                    path.append(node)
                    node = parents[node]
                return path[::-1]

            if visited[current_idx]:
                continue

            visited[current_idx] = True

            for i, neighbor in enumerate(self.nodes[current_idx].neighbors):
                neighbor_idx = self.find_index(neighbor.name)
                edge_cost = self.nodes[current_idx].cost_neighbors[i]

                if not visited[neighbor_idx] and g_values[current_idx] + edge_cost < g_values[neighbor_idx]:
                    g_values[neighbor_idx] = g_values[current_idx] + edge_cost
                    parents[neighbor_idx] = current_idx
                    heapq.heappush(open_set, (g_values[neighbor_idx], neighbor_idx))

        return []  # No path found

# Main function
graph = Graph()

# Creating nodes
for i in range(1, 9):
    graph.nodes.append(Node(i, 0))

# Adding edges and costs
graph.nodes[0].neighbors = [graph.nodes[1], graph.nodes[3], graph.nodes[2]]
graph.nodes[0].cost_neighbors = [2, 3, 10]

graph.nodes[1].neighbors = [graph.nodes[4]]
graph.nodes[1].cost_neighbors = [8]

graph.nodes[2].neighbors = [graph.nodes[6]]
graph.nodes[2].cost_neighbors = [2]

graph.nodes[3].neighbors = [graph.nodes[2], graph.nodes[5]]
graph.nodes[3].cost_neighbors = [2, 4]

graph.nodes[4].neighbors = [graph.nodes[5], graph.nodes[7], graph.nodes[6]]
graph.nodes[4].cost_neighbors = [2, 3, 10]

graph.nodes[5].neighbors = [graph.nodes[4], graph.nodes[6], graph.nodes[7]]
graph.nodes[5].cost_neighbors = [5, 4, 5]

graph.nodes[6].neighbors = [graph.nodes[2], graph.nodes[5], graph.nodes[7]]
graph.nodes[6].cost_neighbors = [2, 5, 1]

graph.nodes[7].neighbors = [graph.nodes[4], graph.nodes[5]]
graph.nodes[7].cost_neighbors = [10, 1]

print("Graph created")

# Call the A* method
solution_path = graph.a_star(1, 8)

if solution_path:
    print("Shortest path cost:", len(solution_path) - 1)
    print("Shortest path:", ' '.join(map(str, solution_path)))
else:
    print("No path found.")
