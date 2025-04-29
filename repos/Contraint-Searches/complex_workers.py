from csp import *

if __name__ == "__main__":
    # Job Assignment Problem
    print("Job Assignment Problem:\n")
    
    job_variables = ['Alice', 'Bob', 'Charlie', 'Diana', 'Eve', 'Frank']
    job_domains = {
        'Alice': ['Painting', 'Plumbing', 'Carpentry'],
        'Bob': ['Painting', 'Carpentry', 'Electrical'],
        'Charlie': ['Plumbing', 'Electrical'],
        'Diana': ['Carpentry', 'Electrical'],
        'Eve': ['Painting', 'Plumbing'],
        'Frank': ['Carpentry', 'Plumbing']
    }
    job_constraints = {
        'Alice': ['Bob', 'Charlie', 'Diana', 'Eve'],
        'Bob': ['Alice', 'Charlie', 'Diana', 'Frank'],
        'Charlie': ['Alice', 'Bob', 'Frank'],
        'Diana': ['Alice', 'Bob', 'Eve'],
        'Eve': ['Alice', 'Frank'],
        'Frank': ['Bob', 'Charlie', 'Eve']
    }
    
    try:
        job_csp = CSP(job_variables, job_domains, job_constraints)
        job_solution = job_csp.solve()
        print(job_solution)
    except Exception as e:
        print("Incomplete problem definition:", e)
    
    print("\n-----------------------------------\n")
