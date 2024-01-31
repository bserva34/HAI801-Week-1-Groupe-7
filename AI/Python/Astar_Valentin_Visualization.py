import sys
import networkx as nx
import matplotlib
matplotlib.use('TkAgg')  # or another backend that supports interactivity, like 'Qt5Agg'
import matplotlib.pyplot as plt

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
    nodes = [(start, 0, heuristics[start], start)]  # Remove the initial predecessor
    G = nx.Graph()
    G.add_node(start)
    predecessors = {}  # Initialize predecessors as an empty dictionary
    while (nodes) :
        nodes.sort(key = lambda x : x[2])
        top = nodes.pop(0)
        if (top[0] == end) :
            print("Coût du chemin :", top[1])
            print("Chemin :", top[3])
            return top[1], G, predecessors  # Return the predecessors as well
        
        for edge in edges[top[0]] :
            nodes.append((
                edge[0],
                top[1] + edge[1],
                top[1] + edge[1] + heuristics[edge[0]],
                top[3] + edge[0])
            )
            G.add_edge(top[3], edge[0])
            predecessors[edge[0]] = top[0]  # Update the predecessor for the current node
    
    print("Aucun chemin trouvé")
    return -1, G, None


start = 'A'
end = 'H'
cost, G, predecessors = aStar(start, end, heuristics, edges)

pos = nx.spring_layout(G)

# Draw the nodes
nx.draw_networkx_nodes(G, pos, node_color='lightblue', node_size=500)

# Draw the edges
nx.draw_networkx_edges(G, pos)

# Draw the predecessors as well
if predecessors:
    for node, predecessor in predecessors.items():
        if predecessor:
            plt.annotate(predecessor, xy=pos[node], xytext=pos[predecessor], arrowprops=dict(arrowstyle="->", color='red'))

# Remove the black edges
edges_to_remove = []
for edge in G.edges():
    if edge[0] == start or edge[1] == end:
        edges_to_remove.append(edge)
G.remove_edges_from(edges_to_remove)

# Draw only one node per node
nx.draw_networkx_labels(G, pos)

plt.title("A* Algorithm Visualization")
plt.show()