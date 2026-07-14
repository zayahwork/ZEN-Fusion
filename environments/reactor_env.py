"""
ZEN Fusion Reactor Environment

A simplified fusion plasma simulation.

The AI agent observes plasma state
and chooses heating/cooling actions.
"""


import numpy as np


class ReactorEnv:

    def __init__(self):
        self.max_steps = 200
        self.reset()


    def reset(self):

        self.temperature = 500.0
        self.instability = 0.05
        self.step_count = 0

        return self.state()


    def state(self):

        return np.array([
            self.temperature,
            self.instability,
            self.step_count
        ], dtype=np.float32)



    def step(self, action):

        """
        Action:
        -1 = cool plasma
         0 = maintain
        +1 = heat plasma
        """

        self.step_count += 1


        # heating effect
        self.temperature += action * 8


        # instability grows with temperature
        self.instability += (
            abs(action) * 0.01
            + (self.temperature-500)*0.00001
        )


        # natural decay
        self.temperature -= 1


        crashed = self.instability > 1.0


        reward = 0


        if crashed:
            reward = -100

        else:

            # reward stable hot plasma
            reward += self.temperature / 500

            # punish instability
            reward -= self.instability



        done = (
            crashed or
            self.step_count >= self.max_steps
        )


        return (
            self.state(),
            reward,
            done
        )



if __name__ == "__main__":

    env = ReactorEnv()

    state = env.reset()

    print("Initial state:")
    print(state)


    for i in range(10):

        state, reward, done = env.step(1)

        print(
            "Step:",
            i,
            "State:",
            state,
            "Reward:",
            reward
        )

        if done:
            break