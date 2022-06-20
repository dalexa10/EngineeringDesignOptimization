import numpy as np
import openmdao.api as om

class Resistor(om.ExplicitComponent):
    """ Computes current across a resistor using Ohm's law """

    def initialize(self):
        self.options.declare('R', default=1., desc='Resistance in Ohms')

    def setup(self):
        self.add_input('V_in', units='V')
        self.add_input('V_out', units='V')
        self.add_output('I', units='A')

    def setup_partials(self):
        self.declare_partials('I', 'V_in', method='fd')
        self.declare_partials('I', 'V_out', method='fd')

    def compute(self, inputs, outputs):
        deltaV = inputs['V_in'] - inputs['V_out']
        outputs['I'] = deltaV / self.options['R']

class Diode(om.ExplicitComponent):
    """ Computes current across a diode using the Shockley diode equation """

    def initialize(self):
        self.options.declare('Is', default=1e-15, desc='Saturation current in Amps')
        self.options.declare('Vt', default=0.025875, desc='Thermal voltage in Volts')

    def setup(self):
        self.add_input('V_in', units='V')
        self.add_input('V_out', units='V')
        self.add_output('I', units='A')

    def setup_partials(self):
        self.declare_partials('I', 'V_in', method='fd')
        self.declare_partials('I', 'V_out', method='fd')

    def compute(self, inputs, outputs):
        deltaV = inputs['V_in'] - inputs['V_out']
        Is = self.options['Is']
        Vt = self.options['Vt']
        outputs['I'] = Is * (np.exp(deltaV / Vt) - 1)

class Node(om.ImplicitComponent):
    """ Computes voltage residual across a node based on incoming and outgoing current """
    def initialize(self):
        self.options.declare('n_in', default=1, types=int, desc='number of connections with + assumed in')
        self.options.declare('n_out', default=1, types=int, desc='number of current connections + assumed out')

    def setup(self):
        self.add_output('V', val=5., units='V')

        for i in range(self.options['n_in']):
            i_name = 'I_in:{}'.format(i)
            self.add_input(i_name, units='A')

        for i in range(self.options['n_out']):
            i_name = 'I_out:{}'.format(i)
            self.add_input(i_name, units='A')

    def setup_partials(self):
        # Note: no partials are declared wrt 'V' here since the residual does not directly depend on it
        self.declare_partials('V', 'I*', method='fd')

    def apply_nonlinear(self, inputs, outputs, residuals):
        residuals['V'] = 0.0
        for i_conn in range(self.options['n_in']):
            residuals['V'] += inputs['I_in:{}'.format(i_conn)]
        for i_conn in range(self.options['n_out']):
            residuals['V'] -= inputs['I_out:{}'.format(i_conn)]

