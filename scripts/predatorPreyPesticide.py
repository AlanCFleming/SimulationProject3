import math
import matplotlib.pyplot as plt
import dynamics


class PredatorPrey(dynamics.Dynamics):
    def __init__(self, preyBirth, preyDeath, predBirth, predDeath, pestUse, pestDecay, time_step):
        numEquations = 2                            # set the number of state equations

        # set constants
        self.preyInc = preyBirth
        self.preyDec = preyDeath
        self.predInc = predBirth
        self.predDec = predDeath
        self.pestInc = pestUse
        self.pestDec = pestDecay

        super().__init__(numEquations, time_step)   # initialize super class dynamics (Euler Method)

        # create variables to hold the state history for plotting
        self.Q = [[] for i in range(numEquations)]
        self.T = []

    def initialize(self, preyWeight, predWeight):
        # set state variable initial values
        self.q[0] = preyWeight
        self.q[1] = predWeight
        # initialize state history used for plotting
        self.Q = [[self.q[i]] for i in range(len(self.q))]
        self.T = [0.0]

    def advance(self, count):
        # compute "count" updates of the state equations
        for i in range(count):
            self.dq[0] = (self.preyInc * self.q[0]) - (self.preyDec * self.q[0] * self.q[1])
            self.dq[1] = (self.predInc * self.q[0] * self.q[1]) - (self.predDec * self.q[1])
            self.step()
        # save the updated state variables after the "count" updates for plotting
        [self.Q[i].append(self.q[i]) for i in range(len(self.q))]
        self.T.append(self.now())

    def print(self):
        # custom print for current simulation
        print('time={0:10f} prey={1:10f} predator={2:10f}'.format(self.time, self.q[0], self.q[1]))

    def plot(self):
        # custom plot for current simulation
        plt.figure()
        plt.subplot(311)
        plt.plot(self.T, self.Q[0], 'k')
        plt.ylabel('prey')

        plt.subplot(312)
        plt.plot(self.T, self.Q[1], 'r')
        plt.ylabel('predator')

        plt.subplot(313)
        plt.plot(self.T, self.Q[0], 'k', self.T, self.Q[1], 'r--')
        plt.ylabel('prey - predator')
        plt.xlabel('time')

        plt.figure()
        plt.plot(self.Q[0], self.Q[1], 'b')
        plt.ylabel('prey')
        plt.xlabel('predator')

        plt.show()


# set parameters for predator-prey simulation

# parameters describing the simulation time
endTime = 1000.0       # length of simulation (i.e. end time)
dt = 0.01             # time step size used to update state equations

# parameters describing the real system
preyBirth = 0.05
preyDeath = 0.001

predBirth = 0.0005
predDeath = 0.01

pestUse = 0.01
pestDecay = 0.01

initPreyWt = 150.0
initPredWt = 50.0

# create the simulation and initialize state variables
P = PredatorPrey(preyBirth, preyDeath, predBirth, predDeath, pestUse, pestDecay, dt)
P.initialize(initPreyWt, initPredWt)

# run the simulation
displayInterval = 1         # number of state updates before saving state
while P.now() < endTime:
    P.advance(displayInterval)
    P.print()               # call print to see numeric values of state per display interval

P.plot()                    # call custom plot
