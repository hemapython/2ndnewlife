# example for overloading -->it means class can have same name of method but arguments should be different
#class student:
 #def avg(a,b)
#def avg (a,b,c) but in python this concept not exist hence we are utilizing this concept in other way exaple is below

class student:
      def __init__(self,p1,p2):
          self.p1=p1
          self.p2=p2


      def sum(self,a=None,b=None,c=None):
          s=0
          if a!=None and b!=None and c!=None:
              s=a+b+c

          elif a!=None and b!=None:
              s=a+b

          else:
              s=a
          return s

g1=student(67,87)
print(g1.sum(3,5,9))
