from core.zen_reasoner import ZENReasoner



class ZENBridge:


    def __init__(self):

        self.reasoner = ZENReasoner()



    def observe(self,state):

        return self.reasoner.decide(state)