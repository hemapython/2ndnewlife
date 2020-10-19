# this is example for Duck typing in polymorphism
# 4 types of polymorphism
# 1.duck typing
# 2.operator overloading
# 3.method overloading
# 4. method overriding

 ### here i will write both duck typing and operator overriding programs

class duck:
     def quake(self):
         print("am positive")
         print(" i will become good developr")
         print("am good at speaking to otheres")

class parrot:
        def quake(self):
            print("am beuatiful than any others think")
            print("am good at giving an interviews")
            print("i wont care about my interviewer")

class dog:
     def barking(self):
         print("i have to be very smart to stay away from the people")
         print("i should act as i does know anything")
         print("my mentor is anmol, i will just go from this company without giving any clues")
         print("my company i would like to join based on python experiance")

class rabbit:
     def goal(self,silence):
         silence.quake()

silence=parrot()

lop=rabbit()
lop.goal(silence)


