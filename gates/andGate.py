from binaryGate import BinaryGate

class AndGate(BinaryGate):
    def __init__(self, n):
        #python 2
        # super(AndGate, self).__init__(n)
        super().__init__(n)
    
    def performGateLogic(self):
        a = self.getPinA()
        b = self.getPinB()
        if a==1 and b==1:
            print(f"And gate {a}:{b}")
            return 1
        else:
            return 0

        