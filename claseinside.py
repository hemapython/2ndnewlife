class student:

    bebrilliant=5000
    def __init__(self,name,rollno):
        self.name=name
        self.rollno=rollno
        self.lap=self.laptop

    def show(self):
         print(self.name,self.rollno)

    class laptop:
     def __init__(self,brand,ram,cpu):
         self.brand=brand
         self.ram=ram
         self.cpu=cpu

     def show(self):
        print(self.brand,self.ram,self.cpu)


s1=student("john",34)
s2=student("ramya",20)
s1.show()
s2.show()
s2.bebrilliant

 #comp1=s1.laptop()
 #comp2=s2.laptop()
#comp1.show()
comp1=student.laptop("intel","5gb","i5")
comp2=student.laptop("AMD","8gb","i7")
print(comp1.brand,comp2.ram,comp1.cpu)
print(comp2.brand,comp1.ram,comp2.cpu)
comp1.show()









