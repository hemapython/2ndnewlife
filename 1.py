# this testcase if for nested class

class multimedia:

    content=100
    def __init__(self,GFX,display):
        self.GFX=GFX
        self.display=display
        self.kuri=self.security()

    def show(self):
        print(self.GFX,self.display)
        print(s1.kuri.show())   #it's just for calling nested class uisng these function

    class security:

     def __init__(self):
        self.TXT=45
        self.SGX=50


     def show(self):
         print(self.TXT,self.SGX)

    @classmethod
    def catch(cls):
        return cls.content


s1=multimedia("directx","HDMI")
s2=multimedia("directx12","DP")

print(s1.show())
print(s2.show())
print(s1.content)

# below are another method for creating object for nested classes
#comp1=multimedia.security()
#print(comp1.show())














