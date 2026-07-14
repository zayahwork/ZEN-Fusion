import sys
import os

# Add project root to Python path
sys.path.append(
    os.path.dirname(
        os.path.dirname(
            os.path.abspath(__file__)
        )
    )
)


from environments.reactor_env import ReactorEnv
from core.zen_reasoner import ZENReasoner


env = ReactorEnv()

zen = ZENReasoner()


state = env.reset()


print("Starting ZEN Fusion Reactor")
print(state)


for step in range(50):

    decision = zen.reason(state)


    print("\nSTEP:", step)

    print("STATE:")
    print(state)

    print("ZEN:")
    print(decision)


    if decision["action"] == "heat":
        action = 1

    elif decision["action"] == "cool":
        action = -1

    else:
        action = 0


    state, reward, done = env.step(action)


    print("REWARD:", reward)


    if done:
        print("REACTOR TERMINATED")
        break