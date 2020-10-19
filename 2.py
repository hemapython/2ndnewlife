# writing program for constructor inheritance  + class inheritance

class A:
    def __init__(self):
        print("am a A init")

    def feature1(self):
        print("feature1A ")

    def feature2(self):
        print("feature2A")

class C:
    def feature5(self):
        print("feature1C")

class B(A,C):         # class B inherited from A hence all feature we can access from A
    def __init__(self):
        super().__init__()    # to get init function from class A before class B init
        print("am a B init")

    def feature3(self):
        print("feature3B")

    def feature4(self):
        print("feature4B")
        print(super().feature5())

s1=B()
s2=A()
print(s1.feature3())
print(s2.feature2())
print(s1.feature4())

# super() keyword used for accessinf parent methods , wherever init methods are instantiate whenever objects gets ctreted hence no nedd o cal them
