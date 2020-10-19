class A:

    def __init__(self,lavanya,hema):
        self.lavanya=lavanya
        self.hema=hema

    def feature1(self):
        print("print feature1 command")

    def feature2(self):
        print("print feature2 command")
        # inheritance

class B:
    def feature3(self):
           print("print feature3 command")
    #super(A).fea

    def feature4(self):
        print("prnt feature4 command")

h1=B()
print(h1.feature3())
