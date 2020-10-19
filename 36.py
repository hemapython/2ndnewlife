class SBI:
    def __init__(self,work,job):
        self.work=work
        self.job=job

    def __sub__(self,other):
        d1=self.work-self.job
        d2=other.work-other.job
        G3=SBI(d1,d2)

        return G3

    def __ge__(self, other):
        j1=self.work+other.work
        j2=self.job+self.job
        if j1>j2:
            return True
        else:
            return False

    # this method will converts print value of objects in string method
    def __str__(self):
        return '{} {}'.format(self.work,self.job)




G1=SBI(34,12)
G2=SBI(55,90)


if G1>=G2:
    print("G2 is more")
else:
    print("G1 is more")

G3=G1-G2
print(G3.job)

G3=G1-G2
print(G3.work+G3.job)

print(G2) # by default it will cal --str__() hence it will print <__main__.SBI object at 0x03793F28> output
# in order to get print value of objects we have to declare string method please refer above.
