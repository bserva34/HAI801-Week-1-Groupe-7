#include <vector>
#include <queue>
#include <string>
#include <iostream>
#include <limits>
#include <set>
#include <algorithm>

struct Node;

struct Edge{
    int weight = 0;
    int node1;
    int node2;
    Edge(int weight, int node1, int node2) : weight(weight), node1(node1), node2(node2){}
};

struct Node{
    std::string name{};
    int index;
    double gCost = std::numeric_limits<double>::infinity();
    double hCost = 0;

    int parent = -1;

    Node(){}
    Node(std::string name, double hCost) : name(name), hCost(hCost){}

    void SetGCost(double gCost){
        this->gCost = gCost;
    }

    void SetParent(int parent){
        this->parent = parent;
    }

    void SetIndex(int index){
        this->index = index;
    }

    bool operator<(const Node& other) const{
        return gCost + hCost < other.gCost + other.hCost;
    }
};

struct CompareNode {
    bool operator()(Node* const& p1, Node* const& p2) {
        // return "true" if "p1" is ordered before "p2", for example:
        return p1->gCost + p1->hCost > p2->gCost + p2->hCost;
    }
};

struct Graph{
    std::vector<Node> nodes{};
    std::vector<Edge> edges{};

    int AddNode(std::string name, double hCost){
        nodes.emplace_back(name, hCost);
        nodes.back().SetIndex(nodes.size() - 1);
        return nodes.size() - 1;
    }

    void AddEdge(int node1, int node2, int weight){
        std::cout << "Adding edge between " << nodes[node1].name << " and " << nodes[node2].name << std::endl;

        edges.emplace_back(weight, node1, node2);
        edges.emplace_back(weight, node2, node1);
    }

    void Print(){
        for(int i = 0; i < nodes.size(); i++){
            std::cout << nodes[i].name << ": ";
            for(Edge* edge : GetEdges(i)){
                std::cout << nodes[edge->node2].name << " ";
            }
            std::cout << std::endl;
        }
    }

    std::vector<Edge*> GetEdges(int node){
        std::vector<Edge*> result{};
        for(Edge& edge : edges){
            if(edge.node1 == node){
                result.emplace_back(&edge);
            }
        }
        return result;
    }

    Node& GetNode(int node){
        return nodes[node];
    }
};

struct Path{
    std::vector<Node*> nodes;
    int weight;

    void Print(){
        for(Node* node : nodes){
            if (node != nullptr) {
                std::cout << node->name << " ";
            }
        }
        std::cout << std::endl;
    }
};

Path AStar(Graph& graph, int start, int end){
    std::priority_queue<Node*, std::vector<Node*>, CompareNode> queue;
    std::set<Node*> visited;
    Node& startNode = graph.GetNode(start);
    startNode.SetGCost(0);
    queue.push(&startNode);

    Node* current;
    
    while(!queue.empty()){
        current = queue.top();
        queue.pop();
        visited.insert(current);

        if(current->index == end){
            break;
        }

        for(Edge* edge : graph.GetEdges(current->index)){
            Node& node = graph.GetNode(edge->node2);
            if(visited.find(&node) != visited.end()){
                continue;
            }
            double gCost = current->gCost + edge->weight;
            if (gCost < node.gCost) {
                node.SetGCost(gCost);
                node.SetParent(current->index);
                queue.push(&node);
            }
        }
    }

    Path path;
    path.weight = current->gCost;
    while(current->index != start){
        path.nodes.emplace_back(current);
        current = &graph.GetNode(current->parent);
    }
    path.nodes.emplace_back(&graph.GetNode(start));

    std::reverse(path.nodes.begin(), path.nodes.end());

    return path;
}

int main(){
    Graph graph{};
    int a = graph.AddNode("A", 10);
    int b = graph.AddNode("B", 3);
    int c = graph.AddNode("C", 5);
    int d = graph.AddNode("D", 6);
    int e = graph.AddNode("E", 8);
    int f = graph.AddNode("F", 4);
    int g = graph.AddNode("G", 2);
    int h = graph.AddNode("H", 0);

    graph.AddEdge(a, b, 2);
    graph.AddEdge(a, c, 10);
    graph.AddEdge(a, d, 3);
    graph.AddEdge(d, c, 2);
    graph.AddEdge(b, e, 8);
    graph.AddEdge(d, f, 4);
    graph.AddEdge(c, g, 2);
    graph.AddEdge(f, e, 5);
    graph.AddEdge(f, g, 5);
    graph.AddEdge(g, h, 1);
    graph.AddEdge(e, h, 10);

    graph.Print();


    int start = a;
    int end = h;
    Path path = AStar(graph, start, end);

    std::cout << "Path weight: " << path.weight << std::endl;
    std::cout << "Path: ";
    path.Print();

    return 0;
}
