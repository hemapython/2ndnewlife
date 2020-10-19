#this example is for learning an file system in python
# below command is for reading the file
#p1=open("simbu",'r')
#print(p1.read())
#below code is for reading first file
#print(p1.readline(),end="") # to print in next line
#print(p1.readline())
#to just print character from the file(4 will print first 4 characters from the file
#print(p1.readline(4))
# To write in a file
#p2=open("nayanathara",'w')
#p2.write("something something ")
#p2=open("nayanathara",'a')
#p2.write("nothing nothing")

# to copy data from one file to another file
#for data in p1:
 # p2.write(data)
# below code is for writing and reading from jpg image
g1=open("Pancard.jpg","rb")
g2=open("newpan.jpg",'wb')
for photo in g1:
 g2.write(photo)
 print(g2)





