class lipstick:
    brands=3

    def __init__(self,col1,col2,col3,col4):
         self.col1=col2
         self.col2=col2
         self.col3=col3
         self.col4=col4
    @staticmethod
    def longlipstick():
            print("lipstick lenght is more")

    def avg(self):
        print((self.col1+self.col2+self.col3+self.col4)/4)

    @classmethod
    def chinnu(cls):
        print(cls.brands)

    def get_col3(self):
        return(self.col3)

    def set_col3(self,value):
        self.col3=value

lip1= lipstick(23,56,45,67)
lip2 = lipstick(45,23,98,50)
print(lipstick.brands)
print(lipstick.chinnu())
lip2.longlipstick()
print(lipstick.get_col3())






