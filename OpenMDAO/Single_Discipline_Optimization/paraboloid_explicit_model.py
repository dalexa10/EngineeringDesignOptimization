# Import OpenMDAO classes needed to build the model
import openmdao.api as om

# Define a component (Explicit)
# Three methods on the class:
# a) setup: define inputs and outputs
# b) setup_partials: declare partial derivatives. Ask OpenMDAO to approximate partial derivative to finite differences
# c) compute: compute all outputs as function of the inputs

# This part of the code show you how the class Paraboloid was created. Check the attributes and methods
class Paraboloid(om.ExplicitComponent):
    """
    Evaluates the equation f(x,y) = (x-3)^2 + xy + (y+4)^2 - 3
    """
    def setup(self):
        self.add_input('x', val=0.0)
        self.add_input('y', val=0.0)
        self.add_output('f_xy', val=0.0)

    def setup_partials(self):
        # Finite difference all partials
        self.declare_partials('*', '*', method='fd')

    def compute(self, inputs, outputs):
        """
        f(x, y) = (x-3)^2 + xy + (y+4)^2 - 3
        Minimum at: x = 6.6667; y = -7.3333
        """
        x = inputs['x']
        y = inputs['y']
        outputs['f_xy'] = (x - 3.0)**2 + x*y + (y + 4.0)**2 - 3.0

# This part of the code show you the previous code in action

if __name__ == '__main__':
    model = om.Group()
    model.add_subsystem('parab_comp', Paraboloid())

    prob = om.Problem(model)
    prob.setup()

    prob.set_val('parab_comp.x', 3.0)
    prob.set_val('parab_comp.y', -4.0)

    prob.run_model()
    print(prob['parab_comp.f_xy'])

    prob.set_val('parab_comp.x', 5.0)
    prob.set_val('parab_comp.y', -2.0)

    prob.run_model()
    print(prob.get_val('parab_comp.f_xy'))

