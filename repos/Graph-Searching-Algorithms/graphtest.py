from graph import *

def print_solution(text, search_output):
    if search_output.path == None:
        print (text, "didn't find a solution!")
    else:
        s = ""

        while not search_output.path.empty():
            node = search_output.path.remove()

            s = s + node.id + "-"

        print (text + " " + s[:-1] + " with cost " + str(search_output.cost) + " after exploring " + str(search_output.explored_nodes) + " nodes")


# Usage: python "graph test.py"

if __name__ == '__main__':

    # Graph for uninformed search: BFS

    g = Graph()

    g.add_node('S', [['A',5], ['B',2], ['C',4]])
    g.add_node('A', [['D',9], ['E',4]])
    g.add_node('B', [['G',6]])
    g.add_node('C', [['F',2]])
    g.add_node('D', [['H',5]])
    g.add_node('E', [['G',6]])
    g.add_node('F', [['G',1]])
    g.add_node('G', [])
    g.add_node('H', [])

    print (g)

    print("Uninformed search \n")
    print_solution("Breadth-first search", g.bfs('S', 'G'))
    print("\n")

    print("A* search \n")
    print_solution("A* search", g.__astar_search('S','G'))