#include <iostream>
#include <set>
#include <map>
#include <set>
#include <cmath>

struct Node {
  std::string name;
  int g;
  int h;
  Node* parent;
  Node(std::string start) : name(start), g(0), h(heuristic(new Node(start))), parent(nullptr) {}
  Node(std::string name, int g, int h, Node* parent) : name(name), g(g), h(h), parent(parent) {}
};

std::set<Node*> open_set;
std::set<Node*> closed_set;
std::map<Node*, Node*> came_from;

std::string start = "A";
std::string goal = "C";

int heuristic(Node* node) {
  // Calcul de la distance euclidienne entre le nœud et la destination
  int dx = node->name[0] - goal[0];
  int dy = node->name[1] - goal[1];
  return sqrt(dx * dx + dy * dy);
}

Node* a_star(std::map<std::string, std::map<std::string, int>>& graph, std::string start, std::string goal) {
  open_set.insert(new Node(start, 0, heuristic(new Node(start)), nullptr));

  while (!open_set.empty()) {
    Node* current = *(open_set.begin());
    open_set.erase(current);
    closed_set.insert(current);

    if (current->name == goal) {
      return current;
    }

    for (const auto& neighbor : graph[current->name]) {
      Node* neighbor_node = new Node(neighbor.first, current->g + neighbor.second, heuristic(new Node(neighbor.first)), current);

      // Vérifie si le nœud voisin n'a pas déjà été exploré
      if (closed_set.find(neighbor_node) == closed_set.end()) {
        // Vérifie si le nœud voisin est plus court que le nœud le plus court connu
        if (open_set.find(neighbor_node) == open_set.end() || neighbor_node->g < (*open_set.find(neighbor_node))->g) {
          // Ajoute le nœud voisin à la liste des nœuds à explorer
          open_set.insert(neighbor_node);
          // Conserve l'historique des parents des nœuds
          came_from[neighbor_node] = current;
        }
      }
    }
  }

  return nullptr;
}

int main() {
  std::map<std::string, std::map<std::string, int>> graph = {
    {"A", {{"B", 2}, {"C", 3}}},
    {"B", {{"A", 1}, {"C", 2}}},
    {"C", {{"A", 3}, {"B", 1}}},
  };


  Node* path = a_star(graph, start, goal);
  if (path == nullptr) {
    std::cout << "Aucun chemin trouvé" << std::endl;
  } else {
    std::cout << "Chemin trouvé :" << std::endl;
    while (path != nullptr) {
      std::cout << path->name << " ";
      path = path->parent;
    }
    std::cout << std::endl;
  }

  return 0;
}