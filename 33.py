# this topic is for inheritance with constructor(init) method
class A:

    def __init__(self):
        print("its A class init")

    def feature1(self):
        print("print feature 1 methid")

    def feature2(self):
        print("print feature 2 methos ")

class B:
     def __init__(self):
      print("class B init method")


     def feature3(self):
         print("print feature 3 method")

     def feature4(self):
         print("print feature 4 method")


class C(B,A):
    def __init__(self):
        super().__init__()   # we have to use Super() method in order to access init method of other classes
        print("C class init method") # method resolution oder forst it will access leften side class init methos here its class B -->Class C(B,A)


    def feature5(self):
        print('fetaure 5 method')


    def feature6(self):
         print("feature 6 method")

a1=A()  # By the time when we create object the constuctor will execute by itself when obj is created for the class
b1=B()
c1=C()

c1.__init__()
c1.feature4()


#super class - sub class
#parent class - child class


