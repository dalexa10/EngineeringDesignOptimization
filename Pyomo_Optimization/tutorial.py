import pyomo.environ as pe  # Build-in features to construct the model
import pyomo.opt as po      # Solver of the model

# Solver Definition
# GLPK open source solver needs to be installed in your conda environment before running this code.
solver = po.SolverFactory('glpk')  # GNU Linear Programming Kit

# Model (Change if necessary)
model = pe.ConcreteModel()
model.x1 = pe.Var(domain=pe.Binary)
model.x2 = pe.Var(domain=pe.Binary)
model.x3 = pe.Var(domain=pe.Binary)
model.x4 = pe.Var(domain=pe.Binary)
model.x5 = pe.Var(domain=pe.Binary)

obj_exp = 3 * model.x1 + 4 * model.x2 + 5 * model.x3 + 8 * model.x4 + 9 * model.x5
model.obj = pe.Objective(sense=pe.maximize, expr=obj_exp)

con_exp = 2 * model.x1 + 3 * model.x2 + 4 * model.x3 + 5 * model.x4 + 9 * model.x5 <= 20
model.con = pe.Constraint(expr=con_exp)

# Solve and Postprocess
result = solver.solve(model, tee=True)  # Tee, allows you to see the log file in real time

#%%
# Run this cell after running the previous cell

# Access solution
print(pe.value(model.x1))
print(pe.value(model.x2))
print(pe.value(model.x3))
print(pe.value(model.x4))
print(pe.value(model.x5))
print(pe.value(model.obj))
