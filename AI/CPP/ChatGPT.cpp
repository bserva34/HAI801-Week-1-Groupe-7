#include <iostream>
#include <vector>
#include <queue>
#include <climits>
#include <stack>
#include <algorithm>

class Node {
public:
    int name;
    int cost;
    std::vector<Node*> neighbors;
    std::vector<int> cost_neighbors;

    Node(int name, int cost) : name(name), cost(cost) {}
};

class Graph {
public:
    std::vector<Node*> nodes;

    int findIndex(int nodeName) {
        for (size_t i = 0; i < nodes.size(); ++i) {
            if (nodes[i]->name == nodeName) {
                return i;
            }
        }
        return -1;
    }

    bool aStar(int startNode, int goalNode, std::vector<int>& solutionPath) {
        std::priority_queue<std::pair<int, int>, std::vector<std::pair<int, int>>, std::greater<std::pair<int, int>>> openSet;
        std::vector<int> gValues(nodes.size(), INT_MAX);
        std::vector<bool> visited(nodes.size(), false);
        std::vector<int> parents(nodes.size(), -1);

        int startIdx = findIndex(startNode);
        int goalIdx = findIndex(goalNode);

        if (startIdx == -1 || goalIdx == -1) {
            std::cerr << "Invalid start or goal node." << std::endl;
            return false;
        }

        openSet.push({0, startIdx});
        gValues[startIdx] = 0;

        while (!openSet.empty()) {
            int currentIdx = openSet.top().second;
            openSet.pop();

            if (currentIdx == goalIdx) {
                // Reconstruct the path
                int node = goalIdx;
                while (node != -1) {
                    solutionPath.push_back(node);
                    node = parents[node];
                }
                std::reverse(solutionPath.begin(), solutionPath.end());
                return true;
            }

            if (visited[currentIdx]) {
                continue;
            }

            visited[currentIdx] = true;

            for (size_t i = 0; i < nodes[currentIdx]->neighbors.size(); ++i) {
                int neighborIdx = findIndex(nodes[currentIdx]->neighbors[i]->name);
                int edgeCost = nodes[currentIdx]->cost_neighbors[i];

                if (!visited[neighborIdx] && gValues[currentIdx] + edgeCost < gValues[neighborIdx]) {
                    gValues[neighborIdx] = gValues[currentIdx] + edgeCost;
                    parents[neighborIdx] = currentIdx;
                    openSet.push({gValues[neighborIdx], neighborIdx});
                }
            }
        }

        return false;  // No path found
    }
};

int main() {
    Graph graph;

    // Creating nodes
    for (int i = 1; i <= 8; ++i) {
        graph.nodes.push_back(new Node(i, 0));
    }

    // Adding edges and costs
    graph.nodes[0]->neighbors = {graph.nodes[1], graph.nodes[3], graph.nodes[2]};
    graph.nodes[0]->cost_neighbors = {2, 3, 10};

    graph.nodes[1]->neighbors = {graph.nodes[4]};
    graph.nodes[1]->cost_neighbors = {8};

    graph.nodes[2]->neighbors = {graph.nodes[6]};
    graph.nodes[2]->cost_neighbors = {2};

    graph.nodes[3]->neighbors = {graph.nodes[2], graph.nodes[5]};
    graph.nodes[3]->cost_neighbors = {2, 4};

    graph.nodes[4]->neighbors = {graph.nodes[5], graph.nodes[7], graph.nodes[6]};
    graph.nodes[4]->cost_neighbors = {2, 3, 10};

    graph.nodes[5]->neighbors = {graph.nodes[4], graph.nodes[6], graph.nodes[7]};
    graph.nodes[5]->cost_neighbors = {5, 4, 5};

    graph.nodes[6]->neighbors = {graph.nodes[2], graph.nodes[5], graph.nodes[7]};
    graph.nodes[6]->cost_neighbors = {2, 5, 1};

    graph.nodes[7]->neighbors = {graph.nodes[4], graph.nodes[5]};
    graph.nodes[7]->cost_neighbors = {10, 1};

    std::cout << "Graph created" << std::endl;

    // Call the aStar method
    std::vector<int> solutionPath;
    bool result = graph.aStar(1, 8, solutionPath);

    if (result) {
        std::cout << "Shortest path cost: " << solutionPath.size() - 1 << std::endl;
        std::cout << "Shortest path: ";
        for (int node : solutionPath) {
            std::cout << node << " ";
        }
        std::cout << std::endl;
    } else {
        std::cout << "No path found." << std::endl;
    }

    // Deallocate memory
    for (Node* node : graph.nodes) {
        delete node;
    }

    return 0;
}
