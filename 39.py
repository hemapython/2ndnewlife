
#  this program is for method overloading example
# method overloading means-->class method names are same but no. of arguments are different , this concept is forbidden in python hence implementing as per below pgm
class arun:
    def kiran(self,a=None,b=None,c=None):
        s=0
        if a!=None and b!=None and c!=None:
         s=a+b+c
        elif a!=None and b!=None:
            s=a+b
        else:
            s=a


        return s


d1=arun()
print(d1.kiran(56,34,12))

#below example is for method overriding
#multiple methods with same name and with the same type of parameter can exist this called as method overriding , but this can be accomplished by using inheritence concept in python

class A:
    def show(self):
        print("am A darling")
class B:
    def show(self):
     print("am B darling")

b1=A()
print(b1.show)










