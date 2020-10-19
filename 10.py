#exception handling programm

a=5
b=0

number=int(input("enter the number"))
print(number)

try:
        print("resource open")
        print(a/b)
        rani=int(input("enter the number "))  # by defaualt it will take string value no need of assigning it
        print(rani)

except ZeroDivisionError as e:
         print("can not devide by zero",e)

except ValueError as e:
         print("it can't accept string value instead of  int",e )

except Exception as e:
         print("observed zero division error",e)

else:
         print("if there is no exception in the try block then it will jump to else block to execute the codes of else block")

finally:
         print("i have completed my exception handling concept, i love myself for everything ")



