"""
ZEN Model Core

Reasoning layer of ZEN.
"""


class ZENModel:


    def __init__(self):

        self.name = "ZEN Reasoning Core"



    def reason(self, observation):

        temperature = observation["temperature"]
        pressure = observation["pressure"]


        if temperature < 900:

            action = "heat"

        elif temperature > 1200:

            action = "cool"

        else:

            action = "maintain"



        return {

            "action": action,

            "confidence": 0.95,

            "reason":
            "Maintaining plasma stability"

        }