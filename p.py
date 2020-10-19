class BT:
    num1=100

    def __init__(self,a,b,c):
        self.firstnumber=a
        self.secondnumber=b
        self.thirdnumber=c
        print("init is being called when object is get creates")

    def get(self):
        print("when u r calling classvariables u should either declare with class name or using self keyword ")

    def summation(self):
        return(self.firstnumber+self.secondnumber+self.thirdnumber+self.num1)


obj1=BT(12,12,12)
print(obj1.summation())
print(obj1.get())



