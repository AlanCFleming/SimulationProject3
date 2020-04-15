import math
import matplotlib.pyplot as plt
import dynamics


class SineWave(dynamics.Dynamics):
    def __init__(self, time_step):
        numEquations = 1

        # set constants, if any
        # NONE

        super().__init__(numEquations, time_step)
        # create variable to hold the history for plotting
        self.Q = [[] for i in range(numEquations)]
        self.T = []

    def initialize(self, x):
        # equation state variables
        self.q[0] = x

        # history of the state variables used for plotting
        self.Q = [[self.q[i]] for i in range(len(self.q))]
        self.T = [0.0]

    def advance(self, count):
        # compute "count" updates of the state equations
        for i in range(count):
            self.dq[0] = math.cos(self.time)
            self.step()
        # save the update state variables after the "count" updates for plotting
        [self.Q[i].append(self.q[i]) for i in range(len(self.q))]
        self.T.append(self.now())

    def plot(self):
        plt.figure()
        plt.plot(self.T, self.Q[0], 'k')
        plt.xlabel('time')
        plt.ylabel('sin(time)')
        plt.show()


# set parameters for sine wave simulation

# parameters describing the simulation time
endTime = 6.28              # length of simulation (i.e. end time)
dt = 0.0001                 # time step size used to update state equations

# parameters describing the real system
# NONE

# create the simulation and initialize state variables
s = SineWave(dt)
s.initialize(0.0)

# run the simulation
displayInterval = 10        # number of state updates before saving state
while s.now() < endTime:
    s.advance(displayInterval)
    s.print()               # call print to see numeric values

s.plot()                    # call custom plot
