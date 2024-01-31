import heapq
def astar(graph,start_node,end_node):
    # astar: F=G+H, we name F as f_distance, G as g_distance, 
    # H as heuristic    
    f_distance={node:float('inf') for node in graph}
    f_distance[start_node]=0
    
    g_distance={node:float('inf') for node in graph}
    g_distance[start_node]=0
    
    came_from={node:None for node in graph}
    came_from[start_node]=start_node
    
    queue=[(0,start_node)]    
    while queue:
        current_f_distance,current_node=heapq.heappop(queue)
        if current_node == end_node:
            print('found the end_node')
            return f_distance, came_from
        for next_node,weights in graph[current_node].items():
            temp_g_distance=g_distance[current_node]+weights[0]            
            if temp_g_distance<g_distance[next_node]:                
                g_distance[next_node]=temp_g_distance
                heuristic=weights[1]                
                f_distance[next_node]=temp_g_distance+heuristic
                came_from[next_node]=current_node
                heapq.heappush(queue,(f_distance[next_node],next_node))
    return f_distance, came_from

if __name__ == '__main__':
    graph={
        'A':{'B':[2,3],'C':[10,5],'D':[3,6]},
        'B':{'A':[2,9],'E':[8,8]},
        'C':{'A':[10,9],'D':[2,6],'G':[2,2]},
        'D':{'A':[3,9],'C':[2,5],'F':[4,4]},
        'E':{'B':[8,8],'F':[5,4],'H':[10,2]},
        'F':{'D':[4,6],'E':[5,8],'G':[5,2]},
        'G':{'C':[2,5],'F':[5,4],'H':[1,0]},
        'H':{'E':[10,8],'G':[1,2]}
    }
    distance,chemin = astar(graph,'A','H')
    current = 'H'
    next = ''
    final = 'A'
    cheminfinal=[current]
    while next != final:
        next = chemin[current]
        current=next
        cheminfinal.append(current)
    cheminfinal.reverse()
    print("chemin final:")
    print("->".join(str(cheminfinal)[1:-1].split(',')))

    

'''class Node:
    def __init__(self,nom : str,  voisins, poids, heuristique) -> None:
        self.nom=nom
        self.voisins=voisins
        self.poids=poids
        self.heuristique=heuristique

def find_node(liste_node, nom_node)->Node:
    for node in liste_node:
        if node.nom == nom_node:
            return node

def Astar(liste_node, A, B):
    closedList = []
    openList = liste_node
    current_node = find_node(liste_node, "A")
    g_score = 0
    h_score = current_node.heuristique
    f_score = g_score+h_score
    while openList != []:
        
    return closedList

if __name__ == '__main__':
    liste_node=[
        Node("A", ["B", "D", "C"], [2,3,10], 9),
        Node("B", ["A", "E"], [2,8], 3),
        Node("C", ["A", "D", "G"], [10,2,2], 5),
        Node("D", ["A", "C", "F"], [3,2,4], 6),
        Node("E", ["B", "F", "G"], [8,5,10], 8),
        Node("F", ["D", "E", "G"], [4,5,5], 4),
        Node("G", ["C", "F", "H"], [2,5,1], 2),
        Node("H", ["E", "G"], [10,1], 0)
    ]
    Rep = Astar(liste_node, "A", "H")
    print(Rep)'''