from constraint import *

if __name__ == "__main__":

    # Three college students are taking five courses. Student 1 is taking courses A, C, and D, student 2 is taking courses B, C, and E and student 3 is taking curses A, C, and E
    # Final exams are scheduled on Monday, Tuesday and Wednesday, schedule the final exams so each student takes only one exam per day

    # A: {'Mon', 'Tue'}
    # B: {'Tue', 'Wed'}
    # C: {'Mon', 'Tue'}
    # D: {'Mon', 'Tue', 'Wed'}
    # E: {'Mon', 'Tue', 'Wed'}

    # Variables: Courses 'A', 'B', 'C', 'D', and 'E'

    csp = Problem()

    csp.addVariable('A', ['Mon', 'Tue'])
    csp.addVariable('B', ['Tue', 'Wed'])
    csp.addVariable('C', ['Mon', 'Tue'])
    csp.addVariable('D', ['Mon', 'Tue', 'Wed'])
    csp.addVariable('E', ['Mon', 'Tue', 'Wed'])

    # Constraints: 'A' != 'C' and 'A' != 'D' and 'A' != 'E' and 'B' != 'C' and 'B' != 'E' and 'C' != 'D' and 'C' != 'E'

    # The function scheduling_constraints_1 defines the constraints for courses

    def scheduling_constraints_1(A, B, C, D, E):
        if A != C and A != D and A != E and B != C and B != E and C != D and C != E:
            return True

    csp.addConstraint(scheduling_constraints_1, ['A','B','C','D','E'])

    s = csp.getSolutions()

    for k, day in enumerate(s):
        print('A:{} B:{} C:{} D:{} E:{}'.format(day['A'], day['B'], day['C'], day['D'], day['E']))

    print ("")






