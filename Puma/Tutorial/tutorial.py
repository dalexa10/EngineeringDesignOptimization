import pumapy as puma

# #%% Puma Filter
# ws = puma.import_3Dtiff(puma.path_to_example_file("100_fiberform.tif"), 1.3e-6)
# ws_closing = ws.copy()
# puma.filter_closing(ws_closing, cutoff=(90, 255), size=3)
# ws_binary = ws.copy()
# ws_binary.binarize_range((90, 255))
# puma.compare_slices(ws_binary, ws_closing, 'z', index=1)

# Fibeform import

ws_fiberform = puma.import_3Dtiff(puma.path_to_example_file("200_fiberform.tif"), 1.3e-6)

# 3D Rendering
puma.render_volume(ws_fiberform)
puma.render_volume(ws_fiberform, (100, 225), style='edges', solid_color=(1, 1, 1))
puma.render_contour(ws_fiberform, (100, 225))

# Geometric properties
ws_fiberform.binarize_range((100, 225))
ws_fiberform.porosity(cutoff=(0, 0))

# Workspace manipulation
ws_copy = ws_fiberform.copy()
ws_copy.rotate(45, 'z', reshape=False, boundary_mode='reflect')
puma.compare_slices(ws_fiberform, ws_copy)

# Filtering example: Euclidean distance
ws_copy = ws_fiberform.copy()
puma.filter_edt(ws_copy, cutoff=(1, 1))
puma.render_volume(ws_copy, cutoff=(0.000001, ws_copy.max()), cmap='jet')





# From GitHub
# ws_fiberform = puma.import_3Dtiff(puma.path_to_example_file("200_fiberform.tif"), 1.3e-6)
# ws_fiberform.matrix = ws_fiberform.matrix[50:150, 50:150, 50:150]
# cond_map = puma.IsotropicConductivityMap()
# cond_map.add_material((0, 89), 0.0257)
# cond_map.add_material((90, 255), 12)
# k_eff_x, P_x, q_x = puma.compute_electrical_conductivity(ws_fiberform, cond_map, 'x', 's', tolerance=1e-2, solver_type='cg')