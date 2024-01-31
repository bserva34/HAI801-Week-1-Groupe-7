from typing import Dict, List, Tuple
import heapq

heuristics_t = Dict[str, float]
edges_t = Dict[str, List[Tuple[str, float]]]
info_t = Tuple[str, float, float, str]

def compareQueue(p1: info_t, p2: info_t) -> bool:
    return p1[2] > p2[2]

def aStar(start: str, end: str, heuristics: heuristics_t, edges: edges_t) -> int:
    nodesQueue = []
    heapq.heapify(nodesQueue)
    visited = set()

    heapq.heappush(nodesQueue, (0, heuristics[start], start, start))
    while nodesQueue:
        _, _, current_node, path = heapq.heappop(nodesQueue)

        if current_node == end:
            print("Coût du chemin :", path)
            print("Chemin :", path)
            return path

        if current_node not in visited:
            visited.add(current_node)

            for edge, cost in edges[current_node]:
                if edge not in visited:
                    total_cost = cost + heuristics[edge]
                    heapq.heappush(nodesQueue, (cost, total_cost, edge, path + ' -> ' + edge))

    print("Aucun chemin trouvé")
    return -1

heuristics: heuristics_t = {
    'A': 9.0,
    'B': 5.0,
    'C': 5.0,
    'D': 6.0,
    'E': 8.0,
    'F': 4.0,
    'G': 2.0,
    'H': 0.0
}

edges: edges_t = {
    'A': [('B', 2.0), ('C', 10.0), ('D', 3.0)],
    'B': [('E', 8.0), ('A', 2.0)],
    'C': [('D', 2.0), ('G', 2.0), ('A', 10.0)],
    'D': [('F', 8.0), ('C', 2.0), ('A', 3.0)],
    'E': [('F', 5.0), ('B', 8.0), ('H', 10.0)],
    'F': [('G', 5.0), ('D', 8.0), ('E', 5.0)],
    'G': [('F', 5.0), ('H', 1.0), ('C', 2.0)],
    'H': [('E', 10.0), ('G', 1.0)]
}

aStar('A', 'H', heuristics, edges)
