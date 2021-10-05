import numpy as np
import pumapy as puma
import pyvista as pv
import scipy.ndimage as nd
import os
import sys

# Generating a workspace of randomly placed, intersecting spheres: with the inputs:
#  - size of domain in voxels: (200,200,200)
#  - diameter of each sphere in voxels: 20
#  - porosity of generated material: 0.7
ws_generated = puma.generate_random_spheres((200,200,200), 20, 0.7)

# The voxel length (in meters) of the workspace defaults to 1 micron (1e-6 m).
# To change the voxel length, modify the parameter directly:
ws_generated.voxel_length = 1.3e-6

# Next we will import an example tomography file of size 200^3 and voxel length 1.3e-6
ws_imported = puma.import_3Dtiff(puma.path_to_example_file("200_fiberform.tif"), 1.3e-6)

#%%
# Generating contour (i.e. isosurface) rendering of the computationally generated material
# The grayscale range of the material to be rendered is specified as (128,255) and is inclusive
puma.render_contour(ws_generated, cutoff=(128, 255), notebook=False)

#%%
