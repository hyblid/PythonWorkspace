from unaryGate import UnaryGate

class NotGate(UnaryGate):
    def __init__(self, n):
        super().__init__(n)
    
    def performGateLogic(self):
        value = self.getPin()
        print(f"Not gate {value}")
        if value:
            return 0
        else:
            return 1
        