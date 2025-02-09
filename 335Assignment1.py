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

#List to store results from generated problems
Unsorted_List = []

def GenerateProblem(): #Generate a random linear programming problem and solve, return the results
    m = np.random.randint(min_m,max_m)
    n = np.random.randint(min_n,max_n)
    c = np.random.uniform(min_c, max_c, size=n)
    a = np.random.uniform(min_a,max_a, size=(m,n))
    b = np.random.uniform(min_b, max_b, size=m)
    res = sp.optimize.linprog(-c,A_ub=a,b_ub=b, method='simplex')
    return [res.success,m,n,res.nit]


for i in range(500): #Generating the 500 problems and appending to a list for visual analysis
    Unsorted_List.append(GenerateProblem())


#Question 1 Scatterplot
''' 
sum_mn_values = [entry[1] + entry[2] for entry in Unsorted_List]
res_nit_values = [entry[3] for entry in Unsorted_List]

plt.scatter(sum_mn_values,res_nit_values)
plt.xlabel("Sum of n+m")
plt.ylabel("Number of Iterations")
plt.show()
'''

#Question 2 Scatterplot
'''
sum_m_values = [entry[1] for entry in Unsorted_List]
res_nit_values = [entry[3] for entry in Unsorted_List]

plt.scatter(sum_m_values,res_nit_values)
plt.xlabel("m")
plt.ylabel("Number of Iterations")
plt.show()
'''