#this is operator overloading program which i found as difficult one
class india:

    def __init__(self,m1,m2):
        self.m1=m1
        self.m2=m2

    def __add__(self, other):
        m1=self.m1+other.m1
        m2=self.m2+other.m2
        s3=india(m1,m2)
        return s3
    def __mul__(self, other):
        m1=self.m1*other.m1
        m2=self.m2*other.m2
        s3=india(m1,m2)
        return s3
    def __gt__(self,put):
        m1=self.m1+self.m2
        m2=put.m1+put.m2
        s3=india(m1,m2)
        if m1>m2:
            return True
        else:
            False

    def __str__(self):
        # return self.m1,self.m2 its just gives non string output hence declaring as below code
       return"{} {}".format(self.m1,self.m2)


s1=india(56,45)
s2=india(45,78)

s3=s1*s2 #(india.__add__(s1,s2))
print(s3.m1)
s3=s1+s2
print(s3.m2)

if s1>s2:
    print("s1 wins")
else:
    print("s2 wins")
    print(s1)
    print(s3)
    print(s2)
    # object s1 cant be provide its value since its an class object hence we should declare an __str__() method to get value from s1 object
#behind the background this below things happens if python knowsthe type of ojects but india is unknown oject python doesnt knowhence we are overriding + operator to work eith class ojects
#a=9
#b=4
#print(a,b)=int.__add__(a,b)=a.__str__()
