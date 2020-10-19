dil={34:"hanuma","koti":"monkey",100:"mahi"}
print(dil[34])
print(dil.get(100))
print(dil["koti"])

dil[34]="daya"
print(dil)

dil['koti']="kapi"
print(dil)
print("the end\n""**********************************")

#next program to get the sume of natuaral numbers from 1 to 5
solitude=0
for i in range(1,20):
    solitude=solitude+i
print(solitude)

print("the end\n""**********************************")

# this program demonstrate the example of cotinue and break example
#example 1
i=10

while i>1:
    if i==5:
        break
    if i==7:
        i=i-1
        continue
    print(i)
    i=i-1

print("the end\n""**********************************")

#example 2
it=9

while it>1:
    if it==5:
        it=it-1
        continue
    if it==2:
        break
    print(it)
    it=it-1


print("loop cant process\n*********************************")
def getidea():
    print("i am beutifull girl i have all the capabilities")
    print("i always think positive everything will happen as i thikk")

def sujatha(name):
    print("she is beautifull no doubt on that"+name)

def ranganatha(r,t):
    print(r+t)


getidea()
sujatha("sharmila")
ranganatha(2,8)


























