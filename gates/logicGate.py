class LogicGate:
    def __init__(self, n):
        self.name = n
        self.output = None
        
    def getLabel(self):
        return self.name
    
    def getOutput(self):
        self.output = self.performGateLogic()
        return self.output

    
    
