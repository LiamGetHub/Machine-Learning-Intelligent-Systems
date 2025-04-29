from csp import *

if __name__ == "__main__":
    # Train Scheduling Problem
    print("Train Scheduling Problem:\n")
    
    train_variables = ['T1', 'T2', 'T3', 'T4', 'T5']
    train_domains = {
        'T1': ['Morning', 'Afternoon', 'Evening'],
        'T2': ['Afternoon', 'Evening', 'Night'],
        'T3': ['Morning', 'Afternoon'],
        'T4': ['Morning', 'Evening'],
        'T5': ['Night', 'Morning']
    }
    train_constraints = {
        'T1': ['T2', 'T3', 'T4'],
        'T2': ['T1', 'T3', 'T5'],
        'T3': ['T1', 'T2', 'T4'],
        'T4': ['T1', 'T3'],
        'T5': ['T2']
    }
    
    try:
        train_csp = CSP(train_variables, train_domains, train_constraints)
        train_solution = train_csp.solve()
        print(train_solution)
    except Exception as e:
        print("Incomplete problem definition:", e)
