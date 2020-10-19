# this is regards to the file systms
ganga=open("mydata",'r')
kavya=ganga.readline()
while kavya!="":
    print(kavya,end="")# why i have declared end="" becoz the file "mydata already having 1 enter and this program statements also have 1 enter hence output gap will be more so
    kavya=ganga.readline()

print("\n********************************************************")

# in the below progrma 1. reading a file in list format and putting that in a "consent object"
#2. we can use "for loop when you use readlines() but that not possible using radline().
#.reversing that consent= contenets and writting  those reversed contenets into toes  file using bhadra object

thunga=open("fist.txt","r")
consent=thunga.readlines() # consent objects holds the content of fist..txt file in a lust format['thammaiahshetty\n', 'myna\n', 'rani\n', 'kiran\n', 'priya\n', 'jagadeesh\n']
    #print(consent)
with open("toes","w") as bhadra:
    for i in reversed(consent):
        bhadra.write(i)

    print("when its writting to toes file then the data which is present in the fist will be reversed in toes file/ ouput - please see in toes file because u cant print written file in python ")
print("************************************************************************")


# this program is for reading and writting of jpg files
try:
    photo=open("newpan.jpg","rb")
    click=open("myphoto.jpg","wb")
    for i in photo:
        click.write(i)

except Exception as e:
    print(e)
finally:
    ("i will sure will become an python automataion engeeneer i love myself for wverything")













