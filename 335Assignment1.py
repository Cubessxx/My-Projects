import numpy as np
import scipy as sp
import matplotlib.pyplot as plt

#Constraints to what kind of linear programs we are choosing to analyze
min_m = 1
max_m = 75
min_n = 1
max_n = 75
min_c = -100
max_c = 100
min_a = -100
max_a = 100
min_b = 0
max_b = 10
count = 0
#List to store results from generated problems
Unsorted_List = []
Unsorted_List_Swapped = []
Problem_List = []

#Toggle for Question 5, where generating a swapped version of the problem is also necessary
Question5 = False

def GenerateProblem(seed): #Generate a random linear programming problem from a given seed and solve, return the results
    global a
    m = np.random.randint(min_m,max_m)
    n = np.random.randint(min_n,max_n)
    a = np.random.uniform(min_a,max_a, size=(m,n))
    np.random.seed(seed)
    c = np.random.uniform(min_c, max_c, size=n)
    np.random.seed(seed+1)
    b = np.random.uniform(min_b, max_b, size=m)
    Problem_List.append([m,n,c])
    res = sp.optimize.linprog(-c,A_ub=a,b_ub=b, method='simplex')
    return [res.success,m,n,res.nit]
    

for count in range(500): #Generating the 500 problems and appending to a list for visual analysis
    seed = np.random.randint(0, 1000000) # Generate a random seed for each problem
    problem_results = GenerateProblem(seed)
    Unsorted_List.append(problem_results)
    if Question5 == True: #Generate a problem with m and n swapped if needed(Question 5)
        a_transposed = a.T
        np.random.seed(seed)
        c_swapped = np.random.uniform(min_c, max_c, size=Problem_List[count][0])
        np.random.seed(seed+1)
        b_swapped = np.random.uniform(min_b, max_b, size=Problem_List[count][1])
        res_swapped = sp.optimize.linprog(-c_swapped, A_ub=a_transposed, b_ub=b_swapped, method='simplex')
        Unsorted_List_Swapped.append([res_swapped.success,Problem_List[count][0],Problem_List[count][1],res_swapped.nit])

#Question 1 Scatterplot(Sum of m+n vs iterations)
''' 
sum_mn_values = [entry[1] + entry[2] for entry in Unsorted_List] #List containing values of m+n for each generated problem
iterations_values = [entry[3] for entry in Unsorted_List] #List containing values for iterations for each generated problem

plt.scatter(sum_mn_values,iterations_values, alpha=0.7, edgecolor='k')
plt.xlabel("Sum of n+m")
plt.ylabel("Number of Iterations")
plt.title("Sum of rows and columns(m+n) vs. Iterations")
plt.grid(True, linestyle='--', alpha=0.5)
plt.show()
'''

#Question 2 Scatterplot(m vs iterations)
'''
sum_m_values = [entry[1] for entry in Unsorted_List]      #List containing values for m for each generated problem
iterations_values = [entry[3] for entry in Unsorted_List] #List containing values for iterations for each generated problem

plt.scatter(sum_m_values,iterations_values, alpha=0.7, edgecolor='k')
plt.xlabel("m")
plt.ylabel("Number of Iterations")
plt.title("Number of rows(m) vs. Iterations")
plt.grid(True, linestyle='--', alpha=0.5)
plt.show()
'''

#Question 3 Scatterplot(min(m,n) vs iterations)
'''
min_mn_values = [min(entry[1],entry[2]) for entry in Unsorted_List]     #List containing smallest dimension from m and n for each generated problem
iterations_values = [entry[3] for entry in Unsorted_List]              #List containing values for iterations for each generated problem

plt.scatter(min_mn_values,iterations_values, alpha=0.7, edgecolor='k')
plt.xlabel("Smallest Dimension(min(m,n))")
plt.ylabel("Number of Iterations")
plt.title("Smallest Matrix Dimension vs. Iterations")
plt.grid(True, linestyle='--', alpha=0.5)
plt.show()
'''

#Question 4 Scatterplot(Unbounded/Bounded Problems vs iterations)
'''
# Separate the data based on bounded vs. unbounded
bounded_data = [entry for entry in Unsorted_List if entry[0] == True] 
unbounded_data = [entry for entry in Unsorted_List if entry[0] == False] 
# Extract m+n and iterations values for both types
bounded_mn_values = [entry[1] + entry[2] for entry in bounded_data]
bounded_iterations = [entry[3] for entry in bounded_data]
unbounded_mn_values = [entry[1] + entry[2] for entry in unbounded_data]
unbounded_iterations = [entry[3] for entry in unbounded_data]

plt.scatter(bounded_mn_values, bounded_iterations, color='blue', alpha=0.7, edgecolor='k', label='Bounded')
plt.scatter(unbounded_mn_values, unbounded_iterations, color='red', alpha=0.7, edgecolor='k', label='Unbounded')
plt.xlabel("Sum of n+m")
plt.ylabel("Number of Iterations")
plt.title("Sum of rows and columns (m+n) vs. Iterations(Bounded and Unbounded Distinguished)")
plt.grid(True, linestyle='--', alpha=0.5)
plt.legend(title="Solution Type")
plt.show()
'''

#Question 5 Scatterplot(mxn vs nxm)
'''
product_mn_values = [entry[1] * entry[2] for entry in Unsorted_List] #List containing values of m*n for each generated problem
iterations_values = [entry[3] for entry in Unsorted_List] #List containing values for iterations for each generated problem
swapped_product_mn_values = [entry[1] * entry[2] for entry in Unsorted_List_Swapped] #List containing values of m*n for each swapped generated problem
swapped_iterations_values = [entry[3] for entry in Unsorted_List_Swapped] #List containing values for iterations for each swapped problem
plt.scatter(product_mn_values,iterations_values, alpha=0.7, edgecolor='k', color='blue',label='Default Problem')
plt.scatter(swapped_product_mn_values,swapped_iterations_values, alpha=0.7, edgecolor='k', color='red',label='Swapped Problem')

#Plots diffrence in iterations swapped vs unswapped
#iterations_diffrence_values = [b / a if a != 0 else float('inf') for a, b in zip(iterations_values, swapped_iterations_values)]
#plt.scatter(swapped_product_mn_values,iterations_diffrence_values, alpha=0.4, edgecolor='k', color='Green') 

plt.xlabel("Product of MxN")
plt.ylabel("Number of Iterations")
plt.title("Product of rows and columns(m*n) vs. Iterations")
plt.grid(True, linestyle='--', alpha=0.5)
plt.legend(title="Problem Type")
plt.show()
'''