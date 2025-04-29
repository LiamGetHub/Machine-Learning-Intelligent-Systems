import sys
from localsearch import *

# Usage: python "localsearch test.py" 2 1

if __name__=="__main__":

    if len(sys.argv) == 3:
        total_solutions = int(sys.argv[1])
        show_trace = False if int(sys.argv[2]) == 0 else True
    else:
        total_solutions = 2
        show_trace = True

    #
    # 5x9 grid with 4 fixed spots and max_solutions with minimum cost
    #

    # original search
    #search = LocalSearchPlayground(height=5, width=9, spots=[(0,2), (1,8), (3,0), (4, 3)], solutions=total_solutions)

    #search for problem #1 firefighter placement
    #search = LocalSearchPlayground(height=10, width=10, spots=[(2,2), (6,1), (3,8), (9, 4), (5,2)], solutions=total_solutions)

    #search for number 2, cell tower placement
    search = LocalSearchPlayground(height=5, width=9, spots=[(2,0), (1,8), (3,7), (4, 5)], solutions=total_solutions)


    search.show("Local search \n")

    print("Testing the helper functions...")

    search.test_helper_functions(verbose = True)



    #hill climbing w random restart
    print("\nHill climbing with random restart")

    solution = search.hill_climbing(verbose=show_trace)

    search.show("Final state", solution)



    solution = search.hill_climbing_random_restart()

    search.show("final state", solution)


    # simulated annealing
    print("\nSimulated Anealing")

    solution = search.simulated_annealing(max_iterations=25, threshold=0.5, verbose=show_trace)

    search.show("Final state", solution)

    