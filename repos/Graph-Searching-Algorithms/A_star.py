# A* search uses a heuristic function f(n) to choose the next node to explore
#
#    f(n) = g(n) + h(n)
#
# where:
#
#    g(n) is the actual cost to reach node n from the initial state
#    h(n) is the estimated cost to reach a goal from node n
#
# Depending on the function f(n), A* search behaves as:
#
# - Uniform cost search      f(n) = g(n)
# - Greedy Best-first search f(n) = h(n)
# - A* search                f(n) = g(n) + h(n)

from typing import List

from Search.list import PriorityQueue


@staticmethod
def __uniform_cost(g, h):
  return g

@staticmethod
def __greedy(g,h):
  return h

@staticmethod
def __astar(g, h):
  return g + h

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



#implement these?????

def ucs(self, initail, goal):
  return self.__astar_search(initail, goal, self.__uniform_cost)

def greedy(self, initail, goal):
  return self.__astar_search(initail, goal, self.__greedy)

def astar(self, initail, goal):
  return self.__astar_search(initail, goal, self.__astar)
