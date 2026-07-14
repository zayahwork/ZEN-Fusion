"""
ZEN Reasoning Core

First connection between ZEN Model
and ZEN Fusion environments.
"""


class ZENReasoner:

    def __init__(self):
        self.memory = []



    def observe(self, state):

        temperature = state[0]
        instability = state[1]


        analysis = {
            "temperature": float(temperature),
            "instability": float(instability)
        }


        return analysis



    def reason(self, state):

        analysis = self.observe(state)

        temperature = analysis["temperature"]
        instability = analysis["instability"]


        # temporary reasoning system
        # will be replaced by trained model

        if instability > 0.7:
            action = "cool"

        elif temperature < 700:
            action = "heat"

        else:
            action = "maintain"



        decision = {

            "action": action,

            "confidence": 0.90,

            "analysis": analysis

        }


        self.memory.append(decision)


        return decision