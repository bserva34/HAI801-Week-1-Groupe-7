import sys

heuristics = {
    'A' : 9,
    'B' : 5,
    'C' : 5,
    'D' : 6,
    'E' : 8,
    'F' : 4,
    'G' : 2,
    'H' : 0
}

edges = {
    'A' : [('B', 2), ('C', 10), ('D', 3)],
    'B' : [('E', 8), ('A', 2)],
    'C' : [('D', 2), ('G', 2), ('A', 10)],
    'D' : [('F', 8), ('C', 2), ('A', 3)],
    'E' : [('F', 5), ('B', 8), ('H', 10)],
    'F' : [('G', 5), ('D', 8), ('E', 5)],
    'G' : [('F', 5), ('H', 1), ('C', 2)],
    'H' : [('E', 10), ('G', 1)],
}

def aStar(start, end, heuristics, edges) :
    nodes = [(start, 0, heuristics[start], start)]
    while (nodes) :
        nodes.sort(key = lambda x : x[2])
        top = nodes.pop(0)
        if (top[0] == end) :
            print("Coût du chemin :", top[1])
            print("Chemin :", top[3])
            return top[1]
        
        for edge in edges[top[0]] :
            nodes.append((
                edge[0],
                top[1] + edge[1],
                top[1] + edge[1] + heuristics[edge[0]],
                top[3] + edge[0])
            )
    print("Aucun chemin trouvé")
    return -1

aStar('A', 'H', heuristics, edges)