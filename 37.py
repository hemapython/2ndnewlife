# this program is for duck typing
class hema:
    def clever(self):
        print("hema is clever she wont give up on  what she wants")
        print("it doesn't matter how many days it require for her to accomplish")
        print("but she wont give up until its done")
        print("that is the speciality of hema")

class priya:
    def clever(self):
        print("she is aimed for becoming a SBI PO")
        print("she is more dedicated person towards her goal")
        print("she wont do the things which will distarcts her")
        print("i have hope on her that she will make her dream come true ")

class kiran:
    def foolich(self):
        print("he will not deny if somebody ask for an help , he 24/7 ready to serve people")
        print("he should learn the knack to becoming rich")
        print("he should learn how to rest and i wish him to aquire all the weath the way how he dreamed for")


class old:
    def good(self,fox):
        fox.clever()

fox=priya()
fox=hema()
tiger=old()
tiger.good(fox)


