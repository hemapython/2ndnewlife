#below pgm for creating class,instance and static methods.

class subjects:

    PT="mark is unique"

    def __init__(self,kan,eng,hin):
      self.kan=kan
      self.eng=eng
      self.hin=hin

    def avg(self):
         return((self.hin+self.eng+self.kan)/3)

    def get_kan(self):
        return self.kan
    def set_hin(self,value):
        self.hin=value

    # now am creating class methods in order to access class variable using class method(cls) is key word for it.
    @classmethod
    def getcommon(cls):
        return(cls.PT)

    @staticmethod
    def info():
        print("i became an python programmer am brilliant and talented girl")

m1=subjects(122,45,67)
m2=subjects(76,35,89)
print(m1.getcommon())
#print(m2.set_hin())
print(m1.info())
print(m2.avg())




