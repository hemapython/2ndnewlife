# this program for file system lets see what am remembered
f=open("mydata","r")
#print(f.readline())
#print(f.read(4))
#print(f.read())
#print(f.readline(4))

f1=open("koli","w")
for go in f:
    print (f1.write(go))

h1=open("deva.jpg","rb")
h2=open("kariya.jpg","wb")
for jinke in h1:
 h2.write(jinke)