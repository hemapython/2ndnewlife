# this progrsm is for operator overloading example

class lion:
    def __init__(self,n1,n2):
        self.n1=n1
        self.n2=n2

    def __add__(self, other):
     jakkle1 = self.n1+other.n1
     jakkle2 = self.n2+other.n2
     hh=lion(jakkle1,jakkle2)
     return hh

    def __floordiv__(self, other):
        gog1=self.n1//self.n2
        gog2=other.n1//other.n2
        hh=lion(gog1,gog2)
        return hh

    def __eq__(self, other):
        jo1=self.n1+self.n2
        jo2=other.n1+other.n2
        if jo1 == jo2:
            return True
        else:
             return False


    def __str__(self):
        return "{} {}".format(self.n1,self.n2)

dog=lion(45,5)
ant=lion(90,5)

hh=dog+ant
print(hh.n2+hh.n1)

if dog==ant:
    print("both are same")
else:
    print("both are different")

hh=dog//ant
print(hh.n2//hh.n1)

print(dog)
print(ant)









