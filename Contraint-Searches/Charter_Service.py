
from constraint import *

if __name__ == "__main__":
    # An air charter service company has 4 private jets. The company must schedule 12 trips next three days for routes A, B, C, D, E, F and G
    # Consider one flight per day for each jet

    # '1': {'A', 'B', 'C'}
    # '2': {'B', 'D', 'E'}
    # '3': {'C', 'E', 'F'}
    # '4': {'E', 'F', 'G'}

    # Variables: Routes 'A', 'B', 'C', 'D', 'E', 'F', 'G'
    

    csp = Problem()

    csp.addVariable('1', ['A', 'B', 'C'])
    csp.addVariable('2', ['B', 'D', 'E'])
    csp.addVariable('3', ['C', 'E', 'F'])
    csp.addVariable('4', ['E', 'F', 'G'])


    # The function scheduling_constraints_1 defines the constraints for courses

    def scheduling_constraints_2(1, 2, 3, 4):
        if 1 != 2 and 1!=3 and 1!=4 and 2!=3 and 2!=4 and 3!= 4:
            return True

    csp.addConstraint(scheduling_constraints_2, ['1', '2', '3', '4'])

    s = csp.getSolutions()

    for k, day in enumerate(s):
        print('A:{} B:{} C:{} D:{} E:{}'.format(day['A'], day['B'], day['C'], day['D'], day['E']))

    print ("")






