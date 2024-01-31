#include <iostream>
#include <queue>
#include <vector>
#include <unordered_map>
#include <utility>
#include <algorithm>

// Heuristic and edges
const std::unordered_map<char, int> heuristics = {
    {'A', 9},
    {'B', 5},
    {'C', 5},
    {'D', 6},
    {'E', 8},
    {'F', 4},
    {'G', 2},
    {'H', 0}
};

const std::unordered_map<char, std::vector<std::pair<char, int>>> edges = {
    {'A', {{'B', 2}, {'C', 10}, {'D', 3}}},
    {'B', {{'E', 8}, {'A', 2}}},
    {'C', {{'D', 2}, {'G', 2}, {'A', 10}}},
    {'D', {{'F', 8}, {'C', 2}, {'A', 3}}},
    {'E', {{'F', 5}, {'B', 8}, {'H', 10}}},
    {'F', {{'G', 5}, {'D', 8}, {'E', 5}}},
    {'G', {{'F', 5}, {'H', 1}, {'C', 2}}},
    {'H', {{'E', 10}, {'G', 1}}}
};

// Function to calculate heuristic
int heuristic(char node, char goal) {
    return heuristics.at(node) + heuristics.at(goal);
}

// Function to perform A* search
std::vector<char> a_star_search(char start, char goal) {
    // Define the priority queue
    auto compare = [&](char lhs, char rhs) {
        return heuristic(lhs, goal) > heuristic(rhs, goal);
    };
    std::priority_queue<char, std::vector<char>, decltype(compare)> queue(compare);

    // Define the maps
    std::unordered_map<char, char> came_from;
    std::unordered_map<char, int> cost_so_far;

    // Initialize the start node
    queue.push(start);
    came_from[start] = start;
    cost_so_far[start] = 0;

    while (!queue.empty()) {
        char current = queue.top();
        queue.pop();

        if (current == goal) {
            break;
        }

        for (auto const &edge : edges.at(current)) {
            char next = edge.first;
            int edge_cost = edge.second;

            int new_cost = cost_so_far[current] + edge_cost;
            if (cost_so_far.count(next) == 0 || new_cost < cost_so_far[next]) {
                cost_so_far[next] = new_cost;
                queue.push(next);
                came_from[next] = current;
            }
        }
    }

    // Construct the path
    std::vector<char> path;
    for (char node = goal; node != start; node = came_from[node]) {
        path.push_back(node);
    }
    path.push_back(start);
    std::reverse(path.begin(), path.end());

    return path;
}

int main() {
    char start = 'A';
    char goal = 'H';
    std::vector<char> path = a_star_search(start, goal);
    for (char node : path) {
        std::cout << node << " ";
    }
    std::cout << std::endl;
    return 0;
}
