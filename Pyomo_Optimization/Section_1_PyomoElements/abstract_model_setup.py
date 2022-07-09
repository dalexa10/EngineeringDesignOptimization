from pyomo.environ import *
import matplotlib.pyplot as plt
import numpy as np
import random

# Structure of the Problem Declaration
model = AbstractModel()
model.x1 = Var(bounds=(0, 4), within=NonNegativeReals)
model.x2 = Var(bounds=(0, 4), within=NonNegativeReals)
model.a11 = Param(mutable=True)

model.eq1 = Constraint(expr=model.a11*model.x1 + 3*model.x2 <= 4)
model.eq2 = Constraint(expr=9*model.x1 + model.x2 <= 6)

model.obj = Objective(expr=3*model.x1 + model.x2, sense=maximize)

# Solve the model
opt = SolverFactory('glpk')
instance = model.create_instance()
instance.a11 = 7  # Mutable parameter
results = opt.solve(instance)  # Solves and updates instance
if (results.solver.status == SolverStatus.ok) and (results.solver.termination_condition ==
                                                   TerminationCondition.optimal):
    print('feasible')
elif (results.solver.termination_condition==TerminationCondition.infeasible):
    print('infeasible')
else:
    print('Solver Status:', results.solver.status)

#%%
instance.eq1.pprint()
instance.eq2.pprint()

#%%
print('X1 = ', value(instance.x1))
print('X2 = ', value(instance.x2))
print('OF = ', value(instance.obj))
