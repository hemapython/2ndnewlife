# writing program for exception handling

#fox=[34,2,1,45,76,45,22,45]
#print(fox[1:5])
#fox=(46,45,[45,12,34,21])
#print(fox.count(45)) # it will give output of how many times 45 present in tuple
#print(fox.index(45))  #it will provide the index number of tuple
#print(fox[2][3])

H=8
J=4
try:
    print(H/J)
    fox=int(input("enter the name"))
    print(fox)
except ZeroDivisionError:
    print("it captures all devide by zero errors")
except ValueError:
    print("it captures all invalid value errors")
except Exception as e:
    print("it captures all the error which not comes under above 2 types of errors")

else:
    print("if there is no exception in try block then it will print else no")
finally:
    ("i can speak elegently i will aquire knowledge that is the only way y i have to come out of my fear , i wil do the things which scares me more")









