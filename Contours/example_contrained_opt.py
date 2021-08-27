import numpy as np
import matplotlib.pyplot as plt
from matplotlib import patheffects

fig, ax = plt.subplots(figsize=(6, 6))

nx = 100
ny = 100

xlow, xhigh = -2, 2
ylow, yhigh = -2, 2

# Set up survey vectors
xvec = np.linspace(xlow, xhigh, nx)
yvec = np.linspace(ylow, yhigh, ny)

# Set up survey matrices.
x1, x2 = np.meshgrid(xvec, yvec)

# Evaluate objective function and constraints
obj = (1 - x1)**2 + (1 - x2)**2 + 0.5*(2*x2 - x1**2)**2
g1 = x1**2 + x2**2 - 1
g2 = -(x1 - 3*x2 + 1/2)

cntr = ax.contour(x1, x2, obj, 10, cmap='coolwarm', colors=None)
ax.clabel(cntr, fmt='%2.1f', use_clabeltext=True)

cg1 = ax.contour(x1, x2, g1, [0], colors='sandybrown')
plt.setp(cg1.collections,
         path_effects=[patheffects.withTickedStroke(angle=90, length=1)])

cg2 = ax.contour(x1, x2, g2, [0], colors='orangered')
plt.setp(cg2.collections,
         path_effects=[patheffects.withTickedStroke(angle=90, length=1)])

ax.set_xlim(xlow, xhigh)
ax.set_ylim(ylow, yhigh)

plt.show()

