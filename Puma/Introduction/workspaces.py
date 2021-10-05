import numpy as np
import pumapy as puma
import pyvista as pv
import scipy.ndimage as nd
import os
import sys

#%%
# This should help regarding workspaces creation (data structures in PuMA environment
# help(puma.Workspace)  # Uncomment this for help in Workspace creation

# Define a workspace instance full of zeros of shape 10x11x12
ws1 = puma.Workspace.from_shape((10, 11, 12))
print(f'Shape of workspace: {ws1.matrix.shape}')
print(f'Unique values in matrix: {ws1.unique_values()}')

# Define a workspace instance  full of custom values (ones) of shape 20x31x212
ws2 = puma.Workspace.from_shape_value((20, 31, 212), 1)
print(f'Shape of workspace: {ws2.matrix.shape}')
print(f'Unique values in matrix: {ws2.unique_values()}')

# Define a workspace of shape 5x6x2, full of a custom value (ones) for the matrix array
# and vectors for the orientation array
ws_w_orient = puma.Workspace.from_shape_value_vector((5, 5, 2), 1, (0.4, 2.0, 5.0))
print(f"Matrix shape of workspace :{ws_w_orient.matrix.shape}")
print(f"Orientation shape of workspace: {ws_w_orient.orientation.shape}")
print("Display Workspace matrix")
ws_w_orient.show_matrix()

print('Display Workspace Orientation')
ws_w_orient.show_orientation()

#%%
# Convert a Numpy array into a Workspace directly
array = np.random.randint(5, size=(10, 10, 10))  # Less than 5 with array (10, 10, 10)
print(array)
ws_array = puma.Workspace.from_array(array)
print("Display Workspace")
ws_array.show_matrix()

# Recall that:
print('To index the matrix array within a Workspace')
print(ws_array[0, 0, 0])  # or
print(ws_array.matrix[0, 0, 0])  # Note same result is obtained


#%%
# Importing a tomography image directly into a workspace (PuMA tomography freely available)
# Important:
# Tiff stack is 8 bit, so the grayscale value will range from 0 to 255. PuMA can also import 16 bit images

ws_raw = puma.import_3Dtiff("data/200_fiberform.tif", 1.3e-6)
print(f"Shape of the Workspace: {ws_raw.matrix.shape}")

# Voxel (3D pixel) length (in meters) of thw workspace can either be set during the import of the Tiff or set
# manually afterwards, as shown below:
ws_raw.voxel_length = 1.3e-6

slices = puma.plot_slices(ws_raw, slice_direction='z', crange=None, cmap='gray', index=1)

#%% Render
# This part needs to be debugged (Matplotlib issue)...
#puma.render_volume(ws_raw, notebook=False)

#%%
