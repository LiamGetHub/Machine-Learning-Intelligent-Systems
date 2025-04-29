"""

The class CSP models a Constraint Satisfaction Problem using a set of variables, domains, and constraints
Variables are represented using a list, while domains and constraints are represented using dictionaries

variables   [variable-1, variable-2, ... , variable-n]
domains     {variable-1: [value-1, value-2, ... value-m], variable-2: [value-1, value-2, ... value-m], ... variable-n: [value-1, value-2, ... value-m]}
constraints {variable-1: [variable-i, variable-i+1, ... ], variable-2: [variable-i, variable-i+1, ... ], ... variable-n: [variable-i, variable-i+1, ... ]}

The function solve() returns a dictionary with the values assigned to each variable: {variable-1: [value], variable-2: [value], ... , variable-n: [value]}

"""

class CSP:
    def __init__(self, variables, domains, constraints):
        self.__variables = variables
        self.__domains = domains
        self.__constraints = constraints

        # validate the problem definition is a complete set of variables, domains, and constraints

        self.__validate_domains_constraints(self.__variables, self.__domains, self.__constraints)

    def __validate_domains_constraints(self, variables, domains, constraints):
        # for each variable, check if there is an entry in the dictionaries representing the domains and the constraints of the problem

        for variable in variables:
            if variable not in domains:
                raise Exception(str("Variable " + variable + " is missing in the dictionary of domains!"))

            if variable not in constraints:
                raise Exception(str("Variable " + variable + " is missing in the dictionary of constraints!"))

    def __select_unassigned_variable(self, variables, domains, assignments):
        # unassigned variables contains the variables without a value (variables not in the dictionary assignments)

        unassigned_variables = [variable for variable in variables if variable not in assignments]

        # return the unassigned variable having the least domain size to reduce failure chances when trying new assignments
        # selecting variables in order or randomly are not efficient strategies, it's better to select variables having less values in their domains

        return min(unassigned_variables, key=lambda variable: len(domains[variable]))

    def __is_consistent(self, variable, value, assignments, constraints):
        # for each constraint variable in constraints, return false if the value of the current variable and the value of the constraint variable are the same, otherwise return true

        for constraint_variable in constraints[variable]:
            if constraint_variable in assignments and assignments[constraint_variable] == value:
                return False

        return True

    def __backtrack(self, variables, domains, constraints, assignments):
        # the search ends when all variables have a value

        if len(assignments) == len(variables):
            return assignments

        # select a variable which is not in assignments and has the least domain size to reduce failure chances when testing new assignments

        variable = self.__select_unassigned_variable(variables, domains, assignments)

        # for each value in the variable domain, check if the assignment is consistent

        for value in domains[variable]:
            if self.__is_consistent(variable, value, assignments, constraints):
                assignments[variable] = value

                result = self.__backtrack(variables, domains, constraints, assignments)

                if result is not None:
                    return result

                # remove the variable from assignments in case the assignment fails

                del assignments[variable]

        return None

    def solve(self):
        return self.__backtrack(self.__variables, self.__domains, self.__constraints, {})
