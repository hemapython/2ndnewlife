# this program am is for binary search
#using an binary search we can improve the manipulation or performans in the pgm , we can leave half of the elements by performing binary serach how
lol=-1
def search(fox,h):
    l=0
    u=len(fox)-1
    while l<len(fox)-1:
        mid=(l+u)//2
        if fox[mid]==h:
            globals()['lol']=mid
            return True
        else:
            if fox[mid]<h:
               l=mid+1
            else:
               u=mid-1
    return False


fox=(11,21,22,34,45,56,78,88)
h=89
if search(fox,h):
    print("element is existed",lol)
else:
    print("element is not existed")





