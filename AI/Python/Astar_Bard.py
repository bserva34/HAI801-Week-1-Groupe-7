class Node:

  def __init__(self, name):
    self.name = name
    self.g = float("inf")
    self.h = float("inf")
    self.parent = None

  def __lt__(self, other):
    return self.f() < other.f()

  def f(self):
    return self.g + self.h
  
def a_star(graph, start, goal, heuristic):
  """
  Recherche le chemin le plus court entre un nœud initial et un nœud final dans un graphe.

  Args:
    graph: Le graphe à parcourir.
    start: Le nœud initial.
    goal: Le nœud final.
    heuristic: Une fonction d'évaluation qui estime la distance restante à parcourir jusqu'à l'arrivée.

  Returns:
    Le chemin le plus court entre les deux nœuds.
  """

  # Initialisation
  open_set = [(0, Node(start))]
  closed_set = []
  came_from = {}

  # Boucle principale
  while open_set:
    # Extraction du nœud le plus prometteur
    _, node = open_set.pop(0)

    # Si le nœud est l'arrivée, on a trouvé le chemin
    if node == goal:
      return reconstruct_path(came_from, goal)

    # Ajout du nœud à la liste des nœuds visités
    closed_set.append(node)

    # Exploration des voisins
    for neighbor, cost in graph[node].items():
      # Si le voisin n'est pas encore visité
      if neighbor not in closed_set:
        # Calcul de la fonction d'évaluation du voisin
        new_g = node.g + cost

        # Si le voisin n'est pas encore dans la liste des nœuds à explorer
        if neighbor not in open_set or new_g < open_set[neighbor][0]:
          # Mise à jour de la fonction d'évaluation du voisin
          open_set.append((new_g, Node(neighbor)))

          # Mise à jour de la distance restante estimée
          neighbor.h = heuristic(neighbor)

          # Ajout du voisin à la liste des nœuds à explorer
          came_from[neighbor] = node

  # Si on arrive ici, c'est que le chemin n'existe pas
  return None


def reconstruct_path(came_from, end):
  """
  Reconstruct le chemin entre un nœud final et le nœud initial.

  Args:
    came_from: Un dictionnaire qui mappe chaque nœud à son prédécesseur.
    end: Le nœud final.

  Returns:
    Le chemin entre les deux nœuds.
  """

  path = [end]
  while end in came_from:
    end = came_from[end]
    path.append(end)
  return path[::-1]


# Définition du graphe
graph = {
  "A": {"B": [2, 3], "C": [10, 5], "D": [3, 6]},
  "B": {"A": [2, 9], "E": [8, 8]},
  "C": {"A": [10, 9], "D": [2, 6], "G": [2, 2]},
  "D": {"A": [3, 9], "C": [2, 5], "F": [4, 4]},
  "E": {"B": [8, 8], "F": [5, 4], "H": [10, 2]},
  "F": {"D": [4, 6], "E": [5, 8], "G": [5, 2]},
  "G": {"C": [2, 5], "F": [5, 4], "H": [1, 0]},
  "H": {"E": [10, 8], "G": [1, 2]}
}

# Définition des nœuds initial et final
start = "A"
goal = "H"

# Définition de l'heuristique
def heuristic(node):
  return abs(node.x - goal.x) + abs(node.y - goal.y)

# Recherche du chemin
path = a_star(graph, start, goal, heuristic)
