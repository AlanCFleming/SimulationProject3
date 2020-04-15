class Dynamics:
    def __init__(self, number_equations, time_step):
        # initialize dynamics
        self.time = 0.0                                 # initialize simulation time
        self.numEqs = number_equations                  # set the number of state equations
        self.dt = time_step                             # set the size of the time step (dt)
        self.q = [0.0 for i in range(self.numEqs)]      # set all state equation values to zero
        self.dq = [0.0 for i in range(self.numEqs)]     # set all derivatives to values of zero

    def now(self):
        return self.time                                # return current simulation time

    def step(self):
        for i in range(0, self.numEqs):
            self.q[i] += self.dq[i] * self.dt           # update state equation i by one time increment (dt)
        self.time += self.dt                            # update simulation time by one time increment (dt)

    def print(self):
        print('time={0:10f}'.format(self.time), end=' ')                 # print simulation time
        for i in range(0, self.numEqs):
            print('q[{0:d}]={1:10f}'.format(i, self.q[i]), end=' ')      # print current value of state equation i
        print(end='\n')

