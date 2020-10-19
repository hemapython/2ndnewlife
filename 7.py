class paper:
    def __init__(self,k1,k2):
        self.k1=k1
        self.k2=k2

    def __sub__(self, other):
        k1=self.k1+self.k2
        k2=other.k1+other.k2
        j3=paper(k1,k2)
        return j3

    def __eq__(self, other):
        r1=self.k1+self.k2
        r2=self.k1+other.k2
        if r1==r2:
             return True
        else:
            False

    def __str__(self):
        return "{} {}".format(self.k1,self.k2)


j1=paper(12,15)
j2=paper(4,7)
j3=j1-j2
print(j1.k1)
print(j2.k2)
print(j2)
print(j3.k1)
print(j3)

if j1==j2:
    print("both are equal")
else:
    print("both are not eqaul")

