#to find out the leap year.

#year=int(input("enter the year"))
#if year%4==0 and year%100!=0:
 #print("year is a leap")
#elif year%400==0:
# print("year is leap year")
#else:
 #print("year is not leap year")

#class home:
 #   def __init__(self):
  #      self.place="hassan"
   #     self.colour= "skyblue"

#house1=home()
#house2=home()
#house1.colour="blue"
#print(house1.colour)
#print(house2.colour)

class vessal:
     def __init__(self):
         self.silver="priya"
         self.aluminium="manu"
     def gold(self):
         self.silver="priya"
         print(self.silver)
     #compare is not inbuilt so creating compare method
     def compare(self,mysore):

        if self.silver==mysore.silver:
         return True
        else :
         return False
hassan=vessal()
mysore=vessal()
#mysore.silver="priya"
if hassan.compare(mysore):
    print("silver is  same")
else:
    print("silver is not same" )
print(hassan.silver)















