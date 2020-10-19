from p import BT


class BLE(BT):
    num2=202

    def __init__(self):
        BT.__init__(self,2,2,2)

    def soon(self):
        print("my intuition saying dont waste time u will sure change job as u will get offer shortly just keep on learn something new do not waste time in nonsense things")

    def getdat(self):
        return(self.num1+self.num2+self.summation())

N1=BLE()
print(N1.getdat())