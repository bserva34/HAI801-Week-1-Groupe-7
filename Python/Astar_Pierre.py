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