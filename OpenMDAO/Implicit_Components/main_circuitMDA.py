from components import *
import openmdao.api as om

class Circuit(om.Group):

    def setup(self):
        self.add_subsystem('n1', Node(n_in=1, n_out=2), promotes_inputs=[('I_in:0', 'I_in')])
        self.add_subsystem('n2', Node())  # Leaving defaults

        self.add_subsystem('R1', Resistor(R=100.), promotes_inputs=[('V_out', 'Vg')])
        self.add_subsystem('R2', Resistor(R=10000.))
        self.add_subsystem('D1', Diode(), promotes_inputs=[('V_out', 'Vg')])

        self.connect('n1.V', ['R1.V_in', 'R2.V_in'])
        self.connect('R1.I', 'n1.I_out:0')
        self.connect('R2.I', 'n1.I_out:1')

        self.connect('n2.V', ['R2.V_out', 'D1.V_in'])
        self.connect('R2.I', 'n2.I_in:0')
        self.connect('D1.I', 'n2.I_out:0')

        self.nonlinear_solver = om.NewtonSolver(solve_subsystems=False)
        self.nonlinear_solver.options['iprint'] = 2
        self.nonlinear_solver.options['maxiter'] = 20
        self.linear_solver = om.DirectSolver()

p = om.Problem()
model = p.model

model.add_subsystem('ground', om.IndepVarComp('V', 0., units='V'))
model.add_subsystem('source', om.IndepVarComp('I', 0.1, units='A'))
model.add_subsystem('circuit', Circuit())

model.connect('source.I', 'circuit.I_in')
model.connect('ground.V', 'circuit.Vg')

p.setup()

# Change NewtonSolver settings in circuit after setup is called
newton = p.model.circuit.nonlinear_solver
newton.options['iprint'] = 2
newton.options['maxiter'] = 500
newton.options['rtol'] = 1e-100
newton.options['solve_subsystems'] = True
newton.linesearch = om.ArmijoGoldsteinLS()
newton.linesearch.options['maxiter'] = 10
newton.linesearch.options['iprint'] = 2

# Initial guesses
p['circuit.n1.V'] = 10.
# p['circuit.n2.V'] = 1.0
p['circuit.n2.V'] = 1e-3

p.run_model()

print(p['circuit.n1.V'])
print(p['circuit.n2.V'])
print(p['circuit.R1.I'])
print(p['circuit.R2.I'])
print(p['circuit.D1.I'])

# Sanity check should sum 0.1 Amps
print(p['circuit.R1.I'] + p['circuit.D1.I'])
