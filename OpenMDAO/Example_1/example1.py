import numpy as np

# Block 1: OpenMDAO and component imports
from openmdao.api import Problem, Group, ScipyOptimizeDriver
from openmdao.api import IndepVarComp, ExecComp
from openmdao.api import NewtonSolver, DirectSolver
from disciplines import Discipline1, Discipline2

# Block 2: creation of all the components and groups except the top-level group
input_comp = IndepVarComp('x')
states_group = Group()
states_group.add_subsystem('discipline1_comp', Discipline1())
states_group.add_subsystem('discipline2_comp', Discipline2())
states_group.connect('discipline1_comp.y1', 'discipline2_comp.y1')
states_group.connect('discipline2_comp.y2', 'discipline1_comp.y2')
states_group.nonlinear_solver = NewtonSolver(iprint=0)
states_group.linear_solver = DirectSolver(iprint=0)
output_comp = ExecComp('f=y1**2-y2+3.')

# Block 3: creation of the top level group
model = Group()
model.add_subsystem('input_comp', input_comp)
model.add_subsystem('states_group', states_group)
model.add_subsystem('output_comp', output_comp)
model.connect('input_comp.x', 'states_group.discipline2_comp.x')
model.connect('states_group.discipline1_comp.y1', 'output_comp.y1')
model.connect('states_group.discipline2_comp.y2', 'output_comp.y2')

# Block 4: specification of the model input (design variable) and the model output (objective)
model.add_design_var('input_comp.x')
model.add_objective('output_comp.f')

# Block 5: creation of the problem and setup
prob = Problem()
prob.model = model
prob.driver = ScipyOptimizeDriver()
prob.setup()

# Block 6: set a model; run the model; and print a model output
prob['input_comp.x'] = 1.0
prob.run_model()
print(prob['output_comp.x'])

# Block 7: solve the optimization problem and print the results
prob.run_driver()
print(prob['input_comp.x'], prob['output_comp.f'])



