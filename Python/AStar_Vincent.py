from queue import PriorityQueue

class Edge:
    def __init__(self, weight, node1_index, node2_index):
        self.weight = weight
        self.node1_index = node1_index
        self.node2_index = node2_index

class Node:
    def __init__(self, name, index, hCost):
        self.name = name
        self.index = index
        self.gCost = 1000000000
        self.hCost = hCost
        self.parent_index = -1

class Graph:
    def __init__(self):
        self.nodes = []
        self.edges = []

    def addNode(self, name, hCost):
        self.nodes.append(Node(name, len(self.nodes), hCost))
        return len(self.nodes) - 1

    def addEdge(self, weight, node1_index, node2_index):
        self.edges.append(Edge(weight, node1_index, node2_index))

    def getEdges(self, node_index):
        edges = []
        for edge in self.edges:
            if edge.node1_index == node_index:
                edges.append(edge)
            elif edge.node2_index == node_index:
                edges.append(edge)
        return edges

    def getNeighbours(self, node_index):
        neighbours = []
        for edge in self.edges:
            if edge.node1_index == node_index:
                neighbours.append(self.nodes[edge.node2_index])
            elif edge.node2_index == node_index:
                neighbours.append(self.nodes[edge.node1_index])
        return neighbours

    def getEdge(self, node1_index, node2_index):
        for edge in self.edges:
            if edge.node1_index == node1_index and edge.node2_index == node2_index:
                return edge
            elif edge.node1_index == node2_index and edge.node2_index == node1_index:
                return edge
        return None

    def getEdgeWeight(self, node1_index, node2_index):
        edge = self.getEdge(node1_index, node2_index)
        if edge is None:
            return None
        return edge.weight

    def getNode(self, node_index):
        for node in self.nodes:
            if node.index == node_index:
                return node
        return None

    def print(self):
        for node in self.nodes:
            print(node.name, ":")
            for neighbour in self.getNeighbours(node.index):
                print("    ", neighbour.name)

class Path:
    def __init__(self, weight):
        self.weight = weight
        self.nodes = []

    def addNode(self, node_index):
        self.nodes.append(node_index)

    def print(self, graph):
        print("Path:")
        for node in self.nodes:
            print("    ", graph.getNode(node).name)

def aStar(graph, start_index, end_index):
    queue = PriorityQueue()
    visited = []
    startNode = graph.getNode(start_index)
    startNode.gCost = 0
    queue.put((0, startNode))

    while not queue.empty():
        currentNode = queue.get()[1]
        if currentNode.index == end_index:
            break
        visited.append(currentNode.index)
        for neighbour in graph.getNeighbours(currentNode.index):
            if neighbour.index in visited:
                continue
            edgeWeight = graph.getEdgeWeight(currentNode.index, neighbour.index)
            if edgeWeight is None:
                continue
            newGCost = currentNode.gCost + edgeWeight
            if newGCost < neighbour.gCost:
                neighbour.gCost = newGCost
                neighbour.parent_index = currentNode.index
                queue.put((neighbour.gCost + neighbour.hCost, neighbour))
    
    path = Path(graph.getNode(end_index).gCost)
    path.addNode(end_index)
    currentNode = graph.getNode(end_index)
    while currentNode.parent_index != -1:
        path.addNode(currentNode.parent_index)
        currentNode = graph.getNode(currentNode.parent_index)
    path.nodes.reverse()
    return path



graph = Graph()
a = graph.addNode("A", 10)
b = graph.addNode("B", 3)
c = graph.addNode("C", 5)
d = graph.addNode("D", 6)
e = graph.addNode("E", 8)
f = graph.addNode("F", 4)
g = graph.addNode("G", 2)
h = graph.addNode("H", 0)

graph.addEdge(2, a, b)
graph.addEdge(10, a, c)
graph.addEdge(3, a, d)
graph.addEdge(2, d, c)
graph.addEdge(8, b, e)
graph.addEdge(4, d, f)
graph.addEdge(2, c, g)
graph.addEdge(5, e, f)
graph.addEdge(5, f, g)
graph.addEdge(1, g, h)
graph.addEdge(10, e, h)

graph.print()

path = aStar(graph, a, h)
print("Path weight:", path.weight)
path.print(graph)
