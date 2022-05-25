from gekko import GEKKO
import numpy as np

# Initialize Model
m = GEKKO()

# help (m)

# Define parameter
eq = m.Param(value=40)

# Initialize variables
x1, x2, x3, x4 = [m.Var() for i in range(4)]

# Initial values
x1.value = 1
x2.value = 5
x3.value = 5
x4.value = 1

# Lower bounds
x1.LOWER = 1
x2.LOWER = 1
x3.LOWER = 1
x4.LOWER = 1

# Upper bounds
x1.UPPER = 5
x2.UPPER = 5
x3.UPPER = 5
x4.UPPER = 5

# Equations
m.Equation(x1 * x2 * x3 * x4 >= 25)
m.Equation(x1**2 + x2**2 + x3**2 + x4**2 == eq)

# Objective function
m.Obj(x1 * x4 * (x1 + x2 + x3) + x3)

# Set global options
m.options.IMODE = 3

# Solve simulation
m.solve(disp=True)

# Results
print('')
print('Results')
print('x1: ' + str(x1.value))
print('x2: ' + str(x2.value))
print('x3: ' + str(x3.value))
print('x4: ' + str(x4.value))
