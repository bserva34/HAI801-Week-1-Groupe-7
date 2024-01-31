import heapq
from collections import defaultdict

def a_star(start, end, heuristics, edges):
    nodes_queue = []
    heapq.heapify(nodes_queue)
    heapq.heappush(nodes_queue, (0, start, 0, start))

    while nodes_queue:
        cost, node, _, path = heapq.heappop(nodes_queue)

        if node == end:
            print("Cost of the path: ", cost)
            print("Path: ", path)
            return cost

        for neighbor in edges[node]:
            new_cost = cost + edges[node][neighbor]
            new_path = path + neighbor
            if (new_cost, neighbor, new_cost, new_path) not in nodes_queue:
                heapq.heappush(nodes_queue, (new_cost, neighbor, new_cost, new_path))

    print("No path found")
    return -1

if __name__ == "__main__":
    heuristics = {
        'A': 9.0,
        'B': 5.0,
        'C': 5.0,
        'D': 6.0,
        'E': 8.0,
        'F': 4.0,
        'G': 2.0,
        'H': 0.0
    }

    edges = {
        'A': {'B': 2.0, 'C': 10.0, 'D': 3.0},
        'B': {'E': 8.0, 'A': 2.0},
        'C': {'D': 2.0, 'G': 2.0, 'A': 10.0},
        'D': {'F': 8.0, 'C': 2.0, 'A': 3.0},
        'E': {'F': 5.0, 'B': 8.0, 'H': 10.0},
        'F': {'G': 5.0, 'D': 8.0, 'E': 5.0},
        'G': {'F': 5.0, 'H': 1.0, 'C': 2.0},
        'H': {'E': 10.0, 'G': 1.0}
    }

    a_star('A', 'H', heuristics, edges)