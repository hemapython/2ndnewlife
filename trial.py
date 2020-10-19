# this is am writting for operator overloading
class sundar:
    def __init__(self,y,e,d):
        #print("my intuition is teeling as i will get job soon")
        self.y=y
        self.e=e
        self.d=d

    def __floordiv__(self, other):
        H1=(self.y/self.d)
        H2=(self.e/other.d)
        H3=other.e/self.e
        G3=sundar(H1,H2,H3)
        return G3

    def __add__(self, other):
        S1=(self.y+self.e+self.d)
        S2=(other.d+other.e+other.y)
        S3=self.d+other.y+self.y
        F3=sundar(S1,S2,S3)
        return F3

    def __str__(self):
        return"{} {} {}".format(self.y,self.e,self.d)









F1=sundar(12,34,12)
F2=sundar(34,56,42)
F3=F1+F2
#print(F3)

G3=F1//F2
print(G3)
















