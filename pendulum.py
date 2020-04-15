import math
import matplotlib.pyplot as plt
import dynamics


class Pendulum(dynamics.Dynamics):
    def __init__(self, pendulum_length, time_step):
        numEquations = 2                            # set the number of state equations

        # set constants, if any
        self.gOverL = 9.802 / pendulum_length

        super().__init__(numEquations, time_step)   # initialize super class dynamics (Euler Method)

        # create variables to hold the state history for plotting
        self.Q = [[] for i in range(numEquations)]
        self.T = []

    def initialize(self, angle, speed):
        # set state variable initial values
        self.q[0] = angle
        self.q[1] = speed
        # initialize state history used for plotting
        self.Q = [[self.q[i]] for i in range(len(self.q))]
        self.T = [0.0]

    def advance(self, count):
        # compute "count" updates of the state equations
        for i in range(count):
            self.dq[0] = self.q[1]
            self.dq[1] = -self.gOverL * math.sin(self.q[0])
            self.step()
        # save the updated state variables after the "count" updates for plotting
        [self.Q[i].append(self.q[i]) for i in range(len(self.q))]
        self.T.append(self.now())

    def print(self):
        # custom print for current simulation
        print('time={0:10f} speed={1:10f} angle={2:10f}'.format(self.time, self.q[1], self.q[0]))

    def plot(self):
        # custom plot for current simulation
        plt.figure()
        plt.subplot(211)
        plt.plot(self.T, self.Q[0], 'k')
        plt.ylabel('angle')

        plt.subplot(212)
        plt.plot(self.T, self.Q[1], 'r')
        plt.ylabel('speed')

        plt.xlabel('time')

        plt.show()


# set parameters for pendulum simulation

# parameters describing the simulation time
endTime = 5.0           # length of simulation (i.e. end time)
dt = 0.0001             # time step size used to update state equations

# parameters describing the real system
length = 1.0            # pendulum length
initial_angle = 2.0     # initial pendulum angle
initial_speed = 0.0     # initial pendulum speed

# create the simulation and initialize state variables
P = Pendulum(length, dt)
P.initialize(initial_angle, initial_speed)

# run the simulation
displayInterval = 250       # number of state updates before saving state
while P.now() < endTime:
    P.advance(displayInterval)
    P.print()               # call print to see numeric values

P.plot()                    # call custom plot
