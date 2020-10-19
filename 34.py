# this is example for Duck typing in polymorphism
# 4 types of polymorphism
# 1.duck typing
# 2.operator overloading
# 3.method overloading
# 4. method overriding

class kiran:

     def __init__(self,f1,f2):
         self.f1=f1
         self.f2=f2


     def __sub__(self, other):
         l1=self.f1-other.f1
         l2=self.f2-other.f2
         s3=kiran(l1,l2)
         return s3


     def __mul__(self, other):
         k1=self.f1*self.f2
         k2=other.f1*other.f2
         s3=kiran(k1,k2)
         return s3
     
     def __str__(self):
         return "{} {}".format(self.f1,self.f2)

s1=kiran(56,34)
s2=kiran(45,23)

#s3=s1-s2

if s1 == s2:
    print("they are same")
else:
    print("they are different")


s3=s1*s2

print(s3.f1,s3.f2)


s3=s1-s2
print(s3.f1-s3.f2)
print(s2)
print(s3)














