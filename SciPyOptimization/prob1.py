import numpy as np
from scipy.optimize import minimize

def objective(x):
    x1 = x[0]
    x2 = x[1]
    x3 = x[2]
    x4 = x[3]
    return x1 * x4 * (x1 + x2 + x3)

def constraint1(x):
    return 25 - x[0] * x[1] * x[2] * x[3]

def constraint2(x):
    for i in range(4):
        sum_sq = 40 - x[i]**2
    return sum_sq

# Initial value (guess)
x0 = [1, 5, 5, 1]
print(objective(x0))

# Bounds
b = (1.0, 5.0)
bnds = (b, b, b, b)
con1 = {'type': 'ineq', 'fun': constraint1}
con2 = {'type': 'eq', 'fun': constraint2}
cons = [con1, con2]

sol = minimize(objective, x0, method='slSQP', bounds=bnds, constraints=cons)
print(sol)
print(sol.x[0])

