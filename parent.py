# this program can give exmple for constructor creation and calling it
class calculator:
    num=50
    def  __init__(self,a,b):
        self.firstname=a
        self.secondname=b
        print("am more healthiest person in the world")

    def getdata(self):
        print("am good python developer")

    def solution(self):
        print(self.firstname+self.secondname+self.num)

s=calculator(20,40)
s.solution()
s.getdata()









