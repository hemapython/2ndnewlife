H1=open("mydata","r")
#print(H1.read())
print(H1.readline(3)) # it will just print the letter numbers from the beginning of text
print(H1.readline())
j1=open("karna","w")
print(j1.write('laptop'))
j1=open("karna","a")
print(j1.write("  mouse and keyboard"))