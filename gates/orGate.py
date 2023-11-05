from binaryGate import BinaryGate

class OrGate(BinaryGate):
    def __init__(self, n):
        super().__init__(n)
    
    def performGateLogic(self):
        a = self.getPinA()
        b = self.getPinB()
        if a==1 or b==1:
            print(f"OR gate {a}:{b}")
            return 1
        else:
            return 0

        