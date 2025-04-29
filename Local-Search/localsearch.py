import math
import random

"""

 The local search playground is a grid with size height x width. When the playground is created, a set of fixed spots defined by their coordinates (x, y) are placed in the grid
 these fixed spots represent real-world objects such as houses, schools, hospitals, pharmacies, police stations, etc.

 For example, the grid below has 5 rows, 9 columns, and four fixed spots (S) at locations {(0,2), (1,8), (3,0), (4, 3)}. Stars represent the grid locations that minimize
 the total distance to the fixed spots. In this example, the minimum total cost from stars to the fixed spots is 6.

  __S______
  __*____*S
  _________
  S*_______
  ___S_____

 Local search algorithms allow to find the optimal coordinates in the grid for a given number of locations, the coordinates (x, y) minimize or maximize the total distance
 from these locations to the fixed spots

 The local search playground may be used to solve local search problems such as finding the minimum distance from a set of public services (e.g. pharmacies, hospitals, etc.) to
 some fixed spots (e.g. houses, schools, etc.) in a neighborhood represented as a grid

 The class LocalSearchPlayground provides the following functions:

 - __available_positions(self) return all available cells in the grid
 - __calculate_cost(self, current_state) calculate the sum of distances from fixed spots to the current state
 - __find_neighbors(self, row, col) return available neighbors for coordinates (row, col)
 - __is_a_fixed_spot(self, row, col) return true if coordinates (row, col) are a spot and false otherwise
 - __random_state(self) return a random state
 - __temperature(self, i) the temperature function used by simulated annealing is a decreasing function T(t) = 1/t
 - hill_climbing(self, max_iterations=25, verbose=True)
 - hill_climbing_random_restart(self, max_iterations=20, verbose=True)
 - simulated_annealing(self, max_iterations=100, verbose=True)
 - show(self, title, solutions=[]) prints out the grid and the solution

 The class LocalSearchPlayground implements three local search algorithms: hill climbing, hill climbing with random restart, and simulated annealing

 - Hill climbing is a simple greedy algorithm that stops when it finds a local maximum by choosing what looks best locally
   The value of the current state is compared with its neighbor states. If any neighbor is better, the current state takes the value of the best neighbor
 - Hill climbing with random restart runs hill climbing multiple times and returns the best solution
 - Simulated annealing is a probabilistic method that approximates the global optimum for an optimization problem in a large search space

"""

class LocalSearchPlayground():
    def __init__(self, height, width, spots, solutions):
        self.__height = height
        self.__width = width
        self.__solutions = solutions
        self.__infinity = float('inf')

        # initialize the coordinates of the fixed spots with pairs (x, y) of the input list spots

        self.__spots = set()

        for spot in spots:
            self.__spots.add((spot[0], spot[1]))

    def __available_positions(self):
        # return all available cells in the grid

        positions = set()

        for row in range(self.__height):
            for col in range(self.__width):
                positions.add((row, col))

        # remove positions occupied by the fixed spots

        for spot in self.__spots:
            positions.remove(spot)

        return positions

    def __calculate_cost(self, current_state):
        # calculate the sum of distances from fixed spots to the current state

        cost = 0

        for spot in self.__spots:
            cost += min(
                abs(spot[0] - current[0]) + abs(spot[1] - current[1])
                for current in current_state
            )

        return cost

    def __find_neighbors(self, row, col):
        available_neighbors = []

        # calculate coordinates for neighbors

        neighbors = [ (row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1) ]

        # check if coordinates (r, c) are valid and it is an available neighbor

        for r, c in neighbors:
            if r >= 0 and r < self.__height and c >= 0 and c < self.__width and not (r, c) in self.__spots and not (r, c) in self.__current_state:
                available_neighbors.append((r, c))

        return available_neighbors

    def __is_a_fixed_spot(self, row, col):
        # return true if coordinates (row, col) are a spot and false otherwise

        return (row, col) in self.__spots

    def __random_state(self):
        # return a random state

        random_state = set()

        for i in range(self.__solutions):
            random_state.add(random.choice(list(self.__available_positions())))

        return random_state

    def hill_climbing(self, max_iterations=25, verbose=True):
        # set a random current state

        self.__current_state = self.__random_state()

        # show initial random state

        if verbose:
            self.show("Initial random state", self.__current_state)

        for i in range(max_iterations):
            if verbose:
                print(str(i) + ":", "Cost of the current state is", self.__calculate_cost(self.__current_state), "with solutions", self.__current_state)

            best_neighbors = []
            best_neighbor_cost = self.__infinity

            # explore the neighbors of the current state which has self.__solutions, each solution may have up to 4 neighbors

            for solution in self.__current_state:
                # the operator * works on any iterable object, it unpacks a tuple or a list, *solution unpacks the row and the column of the spot

                solution_neighbors = self.__find_neighbors(*solution)

                # generate set of neighbors

                for current_neighbor in solution_neighbors:
                    neighbor = self.__current_state.copy()
                    neighbor.remove(solution)
                    neighbor.add(current_neighbor)

                    # check if the current neighbor is the best so far

                    cost = self.__calculate_cost(neighbor)

                    # compare the current neighbor's cost with the best neighbor's cost and update the list of best neighbors

                    if cost < best_neighbor_cost:
                        best_neighbor_cost = cost
                        best_neighbors = [neighbor]
                    elif best_neighbor_cost == cost:
                        best_neighbors.append(neighbor)

            # the search ends when the best neighbor's cost is not better than the current state

            if best_neighbor_cost >= self.__calculate_cost(self.__current_state):
                return self.__current_state
            else:
                # update the current state with a random best neighbor

                self.__current_state = random.choice(best_neighbors)


    def hill_climbing_random_restart(self, max_iterations=25, verbose=True):

        best_cost = self.__infinity

        for i in range(max_iterations):

            current_state = self.hill_climbing(verbose=False)
            current_cost = self.__calculate_cost(current_state)

            if verbose:
                print(str(i) + ":", "Cost of the current state is", current_cost, "with solutions", current_state, end="")
                print(", best cost so far is", best_cost, end="")

            if current_cost < best_cost:
                best_cost = current_cost
                best_state = current_state
            
            if verbose:
                print(", new best cost is", best_cost)

        return best_state

    @staticmethod
    def __temperature(t):
        # the temperature function used by simulated annealing is a decreasing function T(t) = 1/t

        return 1/(t*0.003)

    def simulated_annealing(self, max_iterations=100, threshold=0.5, verbose=True):
        # set a random current state

        self.__current_state = self.__random_state()

        best_state = self.__current_state
        best_cost = self.__calculate_cost(self.__current_state)

        # show initial random state

        if verbose:
            self.show("Initial random state", self.__current_state)

        for i in range(max_iterations):
            if verbose:
                print(str(i) + ":", "Cost of the current state is", self.__calculate_cost(self.__current_state), "with solutions", self.__current_state, end="")

            best_neighbors = []
            best_neighbor_cost = self.__infinity

            # explore the neighbors of the current state which has self.__solutions, each solution may have up to 4 neighbors

            for solution in self.__current_state:
                # the operator * works on any iterable object, it unpacks a tuple or a list, *solution unpacks the row and the column of the spot

                solution_neighbors = self.__find_neighbors(*solution)

                # generate set of neighbors

                for current_neighbor in solution_neighbors:
                    neighbor = self.__current_state.copy()
                    neighbor.remove(solution)
                    neighbor.add(current_neighbor)

                    # check if the current neighbor's cost is the best cost found so far

                    cost = self.__calculate_cost(neighbor)

                    if cost < best_neighbor_cost:
                        best_neighbor_cost = cost
                        best_neighbors = [neighbor]
                    elif best_neighbor_cost == cost:
                        best_neighbors.append(neighbor)

            # pick a random neighbor and compare its cost with the cost of the current state

            random_neighbor = random.choice(best_neighbors)

            # delta = cost of the current state - cost of the random neighbor

            delta = self.__calculate_cost(self.__current_state) - self.__calculate_cost(random_neighbor)

            # if delta > 0, update the current state with a better random neighbor
            # if delta < 0, update the current state with a worse random neighbor if probability exp(delta/temperature(i)) >= 50%

            if verbose:
                print(", cost of the random neighbor is",self.__calculate_cost(random_neighbor))

            if delta > 0:

                self.__current_state = random_neighbor

                if verbose:
                    print(" " * len(str(i) + ":"), "Delta", delta, "is > 0, choose a better random neighbor with cost", self.__calculate_cost(self.__current_state), "and solutions", self.__current_state)

            elif delta < 0:

                temp = self.__temperature(i)

                if math.exp(delta/temp) >= threshold:
                    self.__current_state = random_neighbor

                    if verbose:
                        print(" " * len(str(i) + ":"), "Delta", delta, "is < 0, choose a worse random neighbor with cost", self.__calculate_cost(self.__current_state), end="")
                        print(" and probability", round(math.exp(delta/temp), 4))

            # save the best state

            if self.__calculate_cost(self.__current_state) < best_cost:
                best_cost = self.__calculate_cost(self.__current_state)
                best_state = self.__current_state

        return best_state

    def show(self, title, solutions=[]):
        print("\n" + title + "\n")

        for i in range(self.__height):
            for j in range(self.__width):
                if self.__is_a_fixed_spot(i, j):
                    print("S", end="")
                elif (i, j) in solutions:
                    print("*", end="")
                else:
                    print("_", end="")

            print(" ")

        if len(solutions) != 0:
            print("\nBest cost is", self.__calculate_cost(solutions), "with solutions", solutions, "\n")
    
    #wrote in class 1/29
    def test_helper_functions(self, verbose=True) :

        #set a random current state
        self.__current_state = self.__random_state()

        #show initail random state
        if verbose:
            self.show("Initail random state", self.__current_state)

        for solution in self.__current_state:
            print("Solution", solution, "\n")
        
        #explore nodes of each solution (up to 4 neighbors)
        for solution in self.__current_state:
            print("Solution", solution, "has ", end="")

            solution_neighbors = self.__find_neighbors(*solution)

            print("neighbors", solution_neighbors, "\n")

            for current_neighbor in solution_neighbors:

                neighbor = self.__current_state.copy()

                neighbor.remove(solution)
                neighbor.add(current_neighbor)

                print("  Neightbor", current_neighbor, "cost is", self.__calculate_cost(neighbor))

            print("")