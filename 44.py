# write a program for linear searching
pol=-2

def search(code,x):
    i=0
    while i<len(code):
          if code[i]==x:
              globals()['pol']=i
              return 1
          i+=1
    return -1


code=[84,23,12,65,34,22,99,0,45]
x=45
result = search(code,x) # just assigning search method to result variable
if result==1:
    print("element is present")
else:
    print("element is not present")
