#include <iostream>
#include <vector>
#include <stack>
#include <unordered_set>
#include <queue>
#include <algorithm>
#include <unordered_map>
#include <string>
#include <tuple>

using heuristics_t = std::unordered_map<char, double>;
using edges_t = std::unordered_map<char, std::vector<std::pair<char, double>>>;
using info_t = std::tuple<char, double, double, std::string>;

bool compareQueue(const info_t& p1, const info_t& p2) {
    return std::get<2>(p1) > std::get<2>(p2);
}

int aStar(char start, char end, heuristics_t& heuristics, edges_t& edges) {
    std::priority_queue<
        info_t,
        std::vector<info_t>,
        decltype(&compareQueue)
    > nodesQueue(compareQueue);

    nodesQueue.push({start, 0, heuristics[start], {start}});
    while (!nodesQueue.empty()) {
        info_t top{nodesQueue.top()};

        nodesQueue.pop();

        if (std::get<0>(top) == end) {
            std::cout << "Coût du chemin : " << std::get<1>(top) << '\n';
            std::cout << "Chemin : " << std::get<3>(top) << '\n';
            return std::get<1>(top);
        }

        for (auto& edge : edges[std::get<0>(top)]) {
            nodesQueue.push({
                edge.first,
                std::get<1>(top) + edge.second,
                std::get<1>(top) + edge.second + heuristics[edge.first],
                std::get<3>(top) + edge.first
            });
        }
    }

    std::cout << "Aucun chemin trouvé\n";
    return -1;
}

int main() {
    heuristics_t heuristics{
        {'A', 9.0},
        {'B', 5.0},
        {'C', 5.0},
        {'D', 6.0},
        {'E', 8.0},
        {'F', 4.0},
        {'G', 2.0},
        {'H', 0.0}
    };

    edges_t edges{
        {'A', {{'B', 2.0}, {'C', 10.0}, {'D', 3.0}}},
        {'B', {{'E', 8.0}, {'A', 2.0}}},
        {'C', {{'D', 2.0}, {'G', 2.0}, {'A', 10.0}}},
        {'D', {{'F', 8.0}, {'C', 2.0}, {'A', 3.0}}},
        {'E', {{'F', 5.0}, {'B', 8.0}, {'H', 10.0}}},
        {'F', {{'G', 5.0}, {'D', 8.0}, {'E', 5.0}}},
        {'G', {{'F', 5.0}, {'H', 1.0}, {'C', 2.0}}},
        {'H', {{'E', 10.0}, {'G', 1.0}}}
    };

    aStar('A', 'H', heuristics, edges);
}