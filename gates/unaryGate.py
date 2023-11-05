from logicGate import LogicGate

class UnaryGate(LogicGate):
    def __init__(self, n):
        super().__init__(n)
        self.pin = None
        
    def getPin(self):
        if self.pin==None:
            return int(input("Enter Pin input for gate " + self.getLabel()+ "--->"))
        else:
            return self.pin.getFrom().getOutput()
        
    def setNextPin(self, source):
        if self.pin == None:
            self.pin = source
        else:
            print("Cannot Connect: NO EMPTY PINS on this gate")
        
    