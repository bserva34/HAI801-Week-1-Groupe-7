#include <iostream>
#include <vector>
#include <queue>
#include <unordered_map>
#include <algorithm> // Add the missing include directive for the <algorithm> header

using namespace std;

// Define a struct to represent a node in the graph
struct Node {
    char id;
    double heuristic;
    vector<pair<char, double>> edges;
};

// Define a custom comparator for the priority queue
struct CompareNodes {
    bool operator()(const Node& n1, const Node& n2) {
        return n1.heuristic > n2.heuristic;
    }
};

vector<char> astar(const vector<Node>& graph, char start, char goal) {
    priority_queue<Node, vector<Node>, CompareNodes> openSet;
    unordered_map<char, double> gScore;
    unordered_map<char, double> fScore;
    unordered_map<char, char> cameFrom;

    auto findNode = [&graph](char id) {
        return find_if(graph.begin(), graph.end(), [&id](const Node& node) {
            return node.id == id;
        });
    };

    openSet.push(*findNode(start));
    gScore[start] = 0;
    fScore[start] = findNode(start)->heuristic;

    while (!openSet.empty()) {
        Node current = openSet.top();
        openSet.pop();

        if (current.id == goal) {
            vector<char> path;
            char currentId = current.id;
            while (cameFrom.find(currentId) != cameFrom.end()) {
                path.push_back(currentId);
                currentId = cameFrom[currentId];
            }
            path.push_back(start);
            reverse(path.begin(), path.end());
            return path;
        }

        for (const auto& neighbor : current.edges) {
            char neighborId = neighbor.first;
            double neighborCost = neighbor.second;
            double tentativeGScore = gScore[current.id] + neighborCost;

            if (gScore.find(neighborId) == gScore.end() || tentativeGScore < gScore[neighborId]) {
                cameFrom[neighborId] = current.id;
                gScore[neighborId] = tentativeGScore;
                fScore[neighborId] = tentativeGScore + findNode(neighborId)->heuristic;
                openSet.push(*findNode(neighborId));
            }
        }
    }

    return {};
}

int main() {
    // Create a sample graph
    vector<Node> graph = {
        {'A', 9.0, {{'B', 2.0}, {'C', 10.0}, {'D', 3.0}}},
        {'B', 5.0, {{'E', 8.0}, {'A', 2.0}}},
        {'C', 5.0, {{'D', 2.0}, {'G', 2.0}, {'A', 10.0}}},
        {'D', 6.0, {{'F', 8.0}, {'C', 2.0}, {'A', 3.0}}},
        {'E', 8.0, {{'F', 5.0}, {'B', 8.0}, {'H', 10.0}}},
        {'F', 4.0, {{'G', 5.0}, {'D', 8.0}, {'E', 5.0}}},
        {'G', 2.0, {{'F', 5.0}, {'H', 1.0}, {'C', 2.0}}},
        {'H', 0.0, {{'E', 10.0}, {'G', 1.0}}}
    };

    char start = 'A';
    char goal = 'H';

    // Run A* algorithm
    vector<char> path = astar(graph, start, goal);

    // Print the path
    if (!path.empty()) {
        cout << "Path found: ";
        for (char node : path) {
            cout << node << " ";
        }
        cout << endl;
    } else {
        cout << "No path found." << endl;
    }

    return 0;
}