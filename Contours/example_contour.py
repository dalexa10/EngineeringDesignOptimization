import matplotlib.pyplot as plt
import numpy as np

def f(x,y):
    return x**3 + 2*x*y**2 - y**3 - 20*x

x = np.linspace(-5e10, 5e10, 50)
y = np.linspace(-5e10, 5e10, 50)

X, Y = np.meshgrid(x, y)
Z = f(X, Y)

#plt.contour(X, Y, Z, colors='black')
#plt.contour(X, Y, Z, 50, cmap='RdGy')
plt.contourf(X, Y, Z, 50, cmap='RdGy')
plt.colorbar()
plt.show()

