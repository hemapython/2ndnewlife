# write the program on file system in python
#f1=open("mydata","r")
#print(f1.read())
#print(f1.readline())

#f2=open("kanaka","w")
#print(f2.write("am more focused on it i do not want drag anymore for long time "))
#print(f2.write("\n i have ponder only on python nothing else is more important"))

#for j in f1:
 #   f2.write(j)


f3=open("Screenshot (19).png","rb")
#print(f3.read()) # this line print jpg image as binary format in hexadecimal numbers hence we cant read this file s we can copy this info of image into create an other file so then it can be visible see the pic

f4=open("jeevan.png","wb")

for i in f3:
    f4.write(i)
    print(f4)





