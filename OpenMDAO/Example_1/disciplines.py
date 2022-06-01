import numpy as np
from openmdao.api import ExplicitComponent, ImplicitComponent

class Discipline1(ExplicitComponent):
    def setup(self):
        self.add_input('y2')
        self.add_output('y1')
        self.declare_partials('y1', 'y2')

    def compute(self, inputs, outputs):
        outputs['y1'] = inputs['y2'] ** 2

    def compute_partials(self, inputs, partials):
        partials['y1', 'y2'] = 2 * inputs['y2']

class Discipline2(ImplicitComponent):
    def setup(self):
        self.add_input('x')
        self.add_input('y1')
        self.add_output('y2')
        self.declare_partials('y2', 'x')
        self.declare_partials('y2', 'y1')
        self.declare_partials('y2', 'y2')

    def apply_nonlinear(self, inputs, outputs, residuals):
        residuals['y2'] = (np.exp(-inputs['y1'] * outputs['y2']) - inputs['x'] * outputs['y2'])

    def linearize(self, inputs, outputs, partials):
        partials['y2', 'x'] = - outputs['y2']
        partials['y2', 'y1'] = - outputs['y2'] * np.exp(- inputs['y1'] * outputs['y2'])
        partials['y2', 'y2'] = - inputs['y1'] * np.exp(- inputs['y1'] * outputs['y2']) - inputs['x']
