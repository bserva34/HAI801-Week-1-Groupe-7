heuristics = {
    A = 9,
    B = 5,
    C = 5,
    D = 6,
    E = 8,
    F = 4,
    G = 2,
    H = 0
}

edges = {
    A = {{'B', 2}, {'C', 10}, {'D', 3}},
    B = {{'E', 8}, {'A', 2}},
    C = {{'D', 2}, {'G', 2}, {'A', 10}},
    D = {{'F', 8}, {'C', 2}, {'A', 3}},
    E = {{'F', 5}, {'B', 8}, {'H', 10}},
    F = {{'G', 5}, {'D', 8}, {'E', 5}},
    G = {{'F', 5}, {'H', 1}, {'C', 2}},
    H = {{'E', 10}, {'G', 1}},
}

function aStar(start, nodeEnd, heuristics, edges)
    nodes = {{start, 0, heuristics[start], start}}

    while next(nodes) do
        table.sort(nodes, function(a, b) return a[3] < b[3] end)
        local top = table.remove(nodes, 1)

        if top[1] == nodeEnd then
            print("Coût du chemin :", top[2])
            print("Path :", top[4])
            return top[2]
        end

        for _, edge in ipairs(edges[top[1]]) do
            table.insert(nodes, {
                edge[1],
                top[2] + edge[2],
                top[2] + edge[2] + heuristics[edge[1]],
                top[4] .. edge[1]
            })
        end
    end
    print("Aucun chemin trouvé")
    return -1
end

aStar('A', 'H', heuristics, edges)
