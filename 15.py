# linear searching using for loop we can write the program as below

def search(car,x):

 for i in range (len(car)):
     if car[i]==x:
         return 1
 return -1


car=[56,33,1,98,4,76,56]
x=77
#h= [len(car)]
result=search(car,x)
if result==1:
    print("element is present",result)
else:
    print("element is not present")




