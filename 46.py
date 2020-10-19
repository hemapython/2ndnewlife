# pgm is for binary sorting
gaja=-1
def search(shilpa,f):
       l=0
       u=d
       while l<u:
           mid=(l+u)//2
           if shilpa[mid]==f:
               globals()['gaja']=mid
               return 1
           else:
               if shilpa[mid]<f:
                   l=mid+1
               else:
                   u=mid-1
       return -1

shilpa=[21,34,43,47,51,53,55,63,69,74,77,89]
f=55
d=len(shilpa)-1
result=search(shilpa,f)
if result==1:
    print("element is existed",gaja)
else:
     print("element is not existed")