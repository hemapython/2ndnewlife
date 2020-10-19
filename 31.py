class bat:

    dogs=4
    cows=8
    def __init__(self,gold,money,book):
        self.money=money
        self.gold=gold
        self.book=book

    def avg(self):
        return(m1.money+m2.money+m3.money)/3

    @classmethod
    def ccc(cls):
        return cls.cows+cls.dogs

    @staticmethod
    def tiger():
        return ("am static method")


    def compare(self,other):
        if self.book==other.book:
         return True
        else:
            return False

m1=bat(33,22,11)
m2=bat(56,34,23)
m3=bat(78,56,90)

if m1.compare(m2):
    print("both are same" )
else:
    print("both are different")


print(m2.avg())
print(m1.avg())
print(m3.tiger(),m2.ccc(),m2.money)













