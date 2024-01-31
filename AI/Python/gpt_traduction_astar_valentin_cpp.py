import heapq

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
    'A': [('B', 2.0), ('C', 10.0), ('D', 3.0)],
    'B': [('E', 8.0), ('A', 2.0)],
    'C': [('D', 2.0), ('G', 2.0), ('A', 10.0)],
    'D': [('F', 8.0), ('C', 2.0), ('A', 3.0)],
    'E': [('F', 5.0), ('B', 8.0), ('H', 10.0)],
    'F': [('G', 5.0), ('D', 8.0), ('E', 5.0)],
    'G': [('F', 5.0), ('H', 1.0), ('C', 2.0)],
    'H': [('E', 10.0), ('G', 1.0)]
}

def compare_queue(p1, p2):
    return p1[2] > p2[2]

def a_star(start, end, heuristics, edges):
    nodes_queue = []
    heapq.heappush(nodes_queue, (start, 0, heuristics[start], [start]))

    while nodes_queue:
        top = heapq.heappop(nodes_queue)

        if top[0] == end:
            print(f"Coût du chemin : {top[1]}")
            print(f"Chemin : {' -> '.join(top[3])}")
            return top[1]

        for edge in edges[top[0]]:
            heapq.heappush(nodes_queue, (
                edge[0],
                top[1] + edge[1],
                top[1] + edge[1] + heuristics[edge[0]],
                top[3] + [edge[0]]
            ))

    print("Aucun chemin trouvé")
    return -1

# Run A* algorithm
a_star('A', 'H', heuristics, edges)
