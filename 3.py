
class parrot:
    def quak(self):
        print("am parot")
class dove:
      def quak(self):
          print("am a dove")
class pengvin:
    def quak(self):
        print("print am pengvin")
class kuri:
    def fly(self):
        print("print wont fly")

class eagle:
    def code(self,bird):
        bird.quak()

bird=pengvin()

h1=eagle()
print(h1.code(bird))



#eagle(parrot())
#eagle(dove())
#eagle(kuri()) #kuri object-here its refer as object instead of kuri