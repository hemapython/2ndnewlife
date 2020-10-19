#here am taking the properties of parent class with the help inheritance concept in python
from parent import calculator

class sujatha(calculator):
    karana=60

    def __init__(self):
         calculator.__init__(self,20,20)

    def getdatacomp(self):
        print("i will pakka will go to other companies shortly ")

    def funny(self):
      print (self.num + self.karana ,self.solution())

    def __str__(self):
        print("{} {}".format(self.firstname,self.secondname))

dog=sujatha()
(dog.funny())
dog.getdatacomp()

print(dog)
