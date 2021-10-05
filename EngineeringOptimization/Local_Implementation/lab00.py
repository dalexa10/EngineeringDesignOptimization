
# Check this script if you are not familiar with python at all

# Importing packages
import numpy as np
import autograd
from scipy import optimize as sp
import matplotlib.pyplot as plt


## ------ Gradients and Hessians ---------- ##

#%% Scalar function variable
def line(x):
    y = 5 * x + 10
    return y

# Slope of the line
x0 = 1.0
print(autograd.grad(line)(x0))

#%% Multivariable function
def plane(x):
    z = 5 * x[0] + 10 * x[1] + 4
    return z

# Gradient
x0 = np.array([1.0, 2.0])
print(autograd.grad(plane)(x0))

# Hessian
print(autograd.hessian(plane)(x0))


#%% Function with additional inputs
def planeB(x, a, b):
    z = a * x[0] + b * x[1] + 4
    return z

# Autograde will differentiate only wrt first argument (0)
a = 5.0
b = 10.0
print(autograd.grad(planeB, 0)(x0, a, b))

#%% Plotting Section (Simple plot example)
import matplotlib.pyplot as plt

fig, ax = plt.subplots()
ax.plot(np.array([1, 2, 3, 4]),
        np.array([1, 4, 9, 16]))
ax.set_xlabel('x axis')
ax.set_ylabel('y axis')
ax.set_xlim([1.4, 4.2])
plt.show()

#%%