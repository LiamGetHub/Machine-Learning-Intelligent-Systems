import random
from csp import *

if __name__ == "__main__":

    # Three college students are taking five courses. Student 1 is taking courses A, C, and D, student 2 is taking courses B, C, and E and student 3 is taking curses A, C, and E
    # Final exams are scheduled on Monday, Tuesday and Wednesday, schedule the final exams so each student takes only one exam per day

    # A: {'Mon', 'Tue'}
    # B: {'Tue', 'Wed'}
    # C: {'Mon', 'Tue'}
    # D: {'Mon', 'Tue', 'Wed'}
    # E: {'Mon', 'Tue', 'Wed'}

    # Variables: Courses 'A', 'B', 'C', 'D', and 'E'

    variables = ['A', 'B', 'C', 'D', 'E']

    # Domains: Days

    domains = {'A': ['Mon', 'Tue'], 'B': ['Tue', 'Wed'], 'C': ['Mon', 'Tue'], 'D': ['Mon', 'Tue', 'Wed'], 'E': ['Mon', 'Tue', 'Wed']}

    # Constraints: 'A' != 'C' and 'A' != 'D' and 'A' != 'E' and 'B' != 'C' and 'B' != 'E' and 'C' != 'D' and 'C' != 'E'

    constraints = {'A': ['C', 'D', 'E'], 'B': ['C', 'E'], 'C': ['A', 'B', 'D', 'E'], 'D': ['A', 'C'], 'E': ['A', 'B', 'C']}

    try:

        print("Exam scheduling \n")

        csp = CSP(variables, domains, constraints)

        solution = csp.solve()

        print(solution)

    except Exception as e:
        print("Incomplete problem definition:", e)
