# Let's use the component that we defined before
from openmdao.test_suite.components.paraboloid import Paraboloid
import openmdao.api as om

# Build the model
prob = om.Problem()
prob.model.add_subsystem('parab', Paraboloid(), promotes_inputs=['x', 'y'])

# Define the component whose output will be contrained
prob.model.add_subsystem('const', om.ExecComp('g = x + y'), promotes_inputs=['x', 'y'])

# Design variables 'x' and 'y' span components, we need to provide initial value
prob.model.set_input_defaults('x', 3.0)
prob.model.set_input_defaults('y', -4.0)

# Setup the optimization
prob.driver = om.ScipyOptimizeDriver()
prob.driver.options['optimizer'] = 'COBYLA'

prob.model.add_design_var('x', lower=-50, upper=50)
prob.model.add_design_var('y', lower=-50, upper=50)
prob.model.add_objective('parab.f_xy')

# To add a constraint to the model
prob.model.add_constraint('const.g', lower=0, upper=10.)

prob.setup()
prob.run_driver();

# Minimum value
print(prob.get_val('parab.f_xy'))

# Location of the minium
print(prob.get_val('x'))
print(prob.get_val('y'))
