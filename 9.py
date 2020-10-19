#method overriding --> its an type of polymorphism where it can be done by class inherentence concept , class b (a) can access the the feature of super class a

class A:
      def show(self):
          print("am printing an A")
      def method(self,a,b):
          sub=a-b
          return sub

class B(A):
      def show(self):
          print("am print an B")

s1=B()
s1.show()
print(s1.method(6,2))# since class B having  show method it will print the show method of B  if its not existed as below then it will aceess class
  #A show methos

  # class B(A):
  #  pass