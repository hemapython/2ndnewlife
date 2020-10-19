#example for duck typing t\program

class pycharm:
    def execute(self):
        print("pycharm is good ide")
        print("its an amazing when its come to compiling")
        print("its an user friendly ide")

class eclipse:
    def execute(self):
        print("eclipse i used before")
        print("it i used with java+selenium ")
        print("its works amazingly with java + slenium")
        print("that was became an amazing kickstart for learning pgming lanaguge")

class quake:
    def __init__(self,ide):
        ide.execute()

quake(eclipse())
quake(pycharm())


