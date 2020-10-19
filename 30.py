class kariya:
     discard="owth"

     def __init__(self):
         self.name="kiran"
         self.age=27
         print("am tere")

     def compare(self,other):
         if self.name==other.name:
             return True
         else:
             return False

c1=kariya()
c2=kariya()

c2.name="ishanvi"
if c1.compare(c2):
    print("both are same")
else:
    print("both are not same")
print(c2.name)











