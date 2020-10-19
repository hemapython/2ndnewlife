class gold:

    rate=10000
    silver=9000
    def __init__(self,sai,leela,bhima,malapuram):
        self.sai=sai
        self.leela=leela
        self.bhima=bhima
        self.malapuram=malapuram
        self.pla=self.Platinum() # creating an object of inner class in inside of outer class


    def show(self):
        print(self.sai,self.leela,self.bhima,self.malapuram)
        print(vol1.pla.show()) # calling show method of inner class using vol1 object becoz vol1 object can hold all the methods which is having by an gold outer class
        print(vol2.pla.show())
    class Platinum:

     def __init__(self):
        self.rate=20000
        self.colour="similar to steel colour"

     def show(self):
        return(self.rate,self.colour)

vol1=gold(44,55,66,77)
vol2=gold(00,11,22,33)
vol3=gold(90,44,67,32)

#gol1=gold.Platinum()  # creating an object for inner class "platinum"
# for inner class we can create an object in two types pls refer the commnts in order to understand both

print(vol2.show())
print(vol1.show())
#print(gol1.show()) # this u can cal using object gol1




