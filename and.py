
# Creating program for to understand about init and self methods
#self is nothing but object which we are passing we will mention define self for object

class security:

     teammembers= 14
     def __init__(self):
         self.tstarcount=45
         self.fstarcount=56

     def manage(self):
        print(self.fstarcount)

     # As "compare" is not  inbuilt function  we have to create method for it
     def compare(self,other): # self is c1 and other is c2
         if self.fstarcount==other.fstarcount:
              return True
         else:
             return False

c1=security()
c1.tstarcount=45
c2=security()
print(c1.fstarcount)
print(c1.teammembers)

#its when we wanted to compare c1 with c2
if c1.compare(c2):
    print("both t numbers are equal")

else:
    print("they are not equal")

