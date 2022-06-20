import numpy as np
import openmdao.api as om

class SellarDis1(om.ExplicitComponent):
    """
    Component containing discipline 1 - no derivatives version
    """
    def __init__(self, units=None, scaling=None):
        super().__init__()
        self.execution_count = 0
        self._units = units
        self._do_scaling = scaling

    def setup(self):
        if self._units:
            units = 'ft'
        else:
            units = None
        if self._do_scaling:
            ref = .1
        else:
            ref = 1.

        # Global Design Variable
        self.add_input('z', val=np.zeros(2), units=units)

        # Local Design
        self.add_input('x', val=0.0, units=units)

        # Coupling parameter
        self.add_input('y2', val=1.0, units=units)

        # Coupling output
        self.add_output('y1', val=1.0, lower=0.1, upper=1000, units=units, ref=ref)

    def setup_partials(self):
        # Finite Difference everything
        self.declare_partials('*', '*', method='fd')

    def compute(self, inputs, outputs):
        """
        Evaluates de equation
        y1 = z1**2 + z2 + x1 - 0.2 * y2
        """
        z1 = inputs['z'][0]
        z2 = inputs['z'][1]
        x1 = inputs['x']
        y2 = inputs['y2']

        outputs['y1'] = z1**2 + z2 + x1 - 0.2 * y2
        self.execution_count += 1


class SellarDis2(om.ExplicitComponent):
    """
    Component containing Discipline 2 - no derivatives version
    """
    def __init__(self, units=None, scaling=None):
        super().__init__()
        self.execution_count = 0
        self._units = units
        self._do_scaling = scaling

    def setup(self):
        if self._units:
            units = 'inch'
        else:
            units = None
        if self._do_scaling:
            ref = 0.18
        else:
            ref = 1.0

        # Global Design Variable
        self.add_input('z', val=np.zeros(2), units=units)

        # Coupling parameter
        self.add_input('y1', val=1.0, units=units)

        # Coupling output
        self.add_output('y2', val=1.0, lower=0.1, upper=1000, units=units, ref=ref)

    def setup_partials(self):
        # Finite difference everything
        self.declare_partials('*', '*', method='fd')

    def compute(self, inputs, outputs):
        """
        Evaluates the expression
        y2 = y1**0.5 + z1 + z2
        """
        z1 = inputs['z'][0]
        z2 = inputs['z'][1]
        y1 = inputs['y1']
        if y1.real < 0.0:
            y1 *= -1

        outputs['y2'] = y1**.5 + z1 + z2

        self.execution_count +=1