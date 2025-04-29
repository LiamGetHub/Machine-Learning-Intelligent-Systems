from list import *
from searchpath import *

"""

The class Graph is a weighted graph. It is implemented using a dictionary.

Nodes (vertices) are the keys of the dictionary and the list of adjacent nodes is the value associated to the key. The adjacency list cointains the node and the cost.
Heuristics are implemented with a list. Heuristics are used by Greedy Best-first search and A* search.

Graph = { node-1: [[node-1-1, cost-1-1], [node-1-2, cost-1-2] ... [node-1-m, cost-1-m]],
          node-2: [[node-2-1, cost-2-1], [node-2-2, cost-2-2] ... [node-2-m, cost-2-m]],
          ...
          node-n: [[node-n-1, cost-n-1], [node-n-2, cost-n-2] ... [node-n-m, cost-n-m]] }

heuristic = { node-1: [heuristic-1],
              node-2: [heuristic-2],
              ...
              node-n: [heuristic-n] }

The class Graph implements three search algorithms:

- Breadth-first search (BFS) uses a queue as frontier.
- Depth-first search (DFS) uses a stack as frontier.
- A* search uses a priority queue as frontier and uses the heuristic function f(n) = g(n) + h(n).
  The function f(n) combines the actual cost g(n) to reach node n from the initial state, and the heuristic h(n), which is the estimated cost to reach a goal from node n.

"""

class Graph:
    def __init__(self, graph=None, heuristic=None):
        self.__graph = {} if graph is None else graph
        self.__heuristic = {} if heuristic is None else heuristic

    def get_cost(self, source, destination):
        if source in self.__graph:
            for node in self.__graph[source]:
                if (node[0] == destination):
                    return node[1]

        return float('inf')

    def add_node(self, node, edges=None, heuristic=None):
        if node not in self.__graph:
            self.__graph[node] = [] if edges is None else edges
            self.__heuristic[node] = [0] if heuristic is None else heuristic

    def __str__(self):
        graph = "\n{"

        for node in self.__graph:
            graph = graph + "\n'" + node + "': " + str(self.__graph[node]) + ", "

        graph = graph[:-2] + "\n}"

        edges = "{"

        for node in self.__heuristic:
            edges = edges + "'" + node + "':" + str(self.__heuristic[node]) + ", "

        edges = edges[:-2] + "} \n"

        return graph + "\n" + edges if len(edges) > 1 else graph

    def __retrieve_search_path(self, initial, node, explored):
        path = Stack()

        cost = 0

        while node.parent is not None:
            path.add(node)

            cost = cost + self.get_cost(node.parent, node.id)

            node = explored.get(node.parent)

        path.add(Node(initial))

        return SearchPath(path, cost, explored.size())

    # Breadth-first search (BFS) uses a queue as frontier

    def bfs(self, initial, goal):
        # initialize the list of explored nodes

        explored = List()

        frontier = Queue()
        frontier.add(Node(initial))

        while not frontier.empty():
            node = frontier.remove()

            if not explored.contains(node.id):
                explored.add(node)

                # if the goal state is found, return the search path

                if node.id == goal:
                    return self.__retrieve_search_path(initial, node, explored)

                # add successors to the frontier

                successors = self.__graph[node.id]

                # successors is the adjacency list of the current node: [[node-1-1, cost-1-1], [node-1-2, cost-1-2] ... [node-1-m, cost-1-m]]

                for successor in successors:
                    # successor[0] is the node id, and successor[1] is the cost

                    successor_node = successor[0]
                    successor_cost = successor[1]

                    # add successor to the frontier if it has not been explored yet

                    if not explored.contains(successor_node):
                        frontier.add(Node(successor_node, node.id))

        # goal state not found

        return SearchPath()
    def __astar_search(self, initial, goal, algorithm=__astar):
        # initialize the list of explored nodes

        explored = List()

        # A* search uses a priority queue as frontier

        frontier = PriorityQueue()
        frontier.add(Node(initial))

        while not frontier.empty():
            node = frontier.remove()

            if not explored.contains(node.id):
                explored.add(node)

                # if the goal state is found, return the search path

                if node.id == goal:
                    return self.__retrieve_search_path(initial, node, explored)

                # add successors to the frontier

                successors = self.__graph[node.id]

                # successors is the adjacency list of the current node: [[node-1-1, cost-1-1], [node-1-2, cost-1-2] ... [node-1-m, cost-1-m]]

                for successor in successors:
                    # successor[0] is the node id, and successor[1] is the cost

                    successor_node = successor[0]
                    successor_cost = successor[1]

                    # add successor to the frontier if it has not been explored yet

                    if not explored.contains(successor_node):

                        # g(n) represents the actual cost to reach the node from the initial state

                        g = int(node.cost + successor_cost)

                        # h(n) represents the estimated cost to reach a goal state from node n

                        h = int(self.__heuristic[successor_node][0])

                        # f(n) is determined by the algorithm: Uniform cost search uses g(n), Greedy Best-first search uses h(n), and A* search uses g(n) + f(n)

                        f = algorithm(g, h)

                        frontier.add(Node(successor_node, node.id, g, f))

        # goal state not found

        return SearchPath()