
pos=-1
def search(kuri,x):
   i=0
   while i< len(kuri):
       if kuri[i]==x:

             print("am hema")
             #accessing global variable using an globle() 'pos' is global varible name and assigning i value so that in every increment i value will get assign to pos variable
             globals()['pos']=i
             return 1

       i=i+1

   return -1


kuri=[23,56,45,34,77,45]
x=23

result= search (kuri,x)

if (result==1):
    # "here pos+1' means pos will get assign to i value, means here we are trying to print element lenght value using pos+1
     print("element is existed",pos+1)

else:
    print("element not existed")

