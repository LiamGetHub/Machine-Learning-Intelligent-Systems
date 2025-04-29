from csp import *

if __name__ == "__main__":
    # Job Assignment Problem
    print("Job Assignment Problem:\n")
    
    job_variables = ['Alice', 'Bob', 'Charlie']
    job_domains = {
        'Alice': ['Painting', 'Plumbing'],
        'Bob': ['Painting', 'Carpentry'],
        'Charlie': ['Plumbing']
    }
    job_constraints = {
        'Alice': ['Bob', 'Charlie'],
        'Bob': ['Alice', 'Charlie'],
        'Charlie': ['Alice', 'Bob']
    }
    
    try:
        job_csp = CSP(job_variables, job_domains, job_constraints)
        job_solution = job_csp.solve()
        print(job_solution)
    except Exception as e:
        print("Incomplete problem definition:", e)
    
    print("\n-----------------------------------\n")
    
    # Train Scheduling Problem
    print("Train Scheduling Problem:\n")
    
    train_variables = ['T1', 'T2', 'T3']
    train_domains = {
        'T1': ['Morning', 'Afternoon'],
        'T2': ['Afternoon', 'Evening'],
        'T3': ['Morning', 'Afternoon', 'Evening']
    }
    train_constraints = {
        'T1': ['T2', 'T3'],
        'T2': ['T1', 'T3'],
        'T3': ['T1', 'T2']
    }
    
    try:
        train_csp = CSP(train_variables, train_domains, train_constraints)
        train_solution = train_csp.solve()
        print(train_solution)
    except Exception as e:
        print("Incomplete problem definition:", e)
