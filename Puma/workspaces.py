import numpy as np
import pumapy as puma
import pyvista as pv
import scipy.ndimage as nd
import os
import sys

# This should help regarding workspaces creation (data structures in PuMA environment
# help(puma.Workspace)  # Un comment this for help

# Define a workspace full of zeros of shape 10x11x12
ws1 = puma.Workspace.from_shape((10, 11, 12))
print(f'Shape of workspace: {ws1.matrix.shape}')
print(f'Unique values in matrix: {ws1.unique_values()}')