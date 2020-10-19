pos=-1
def search(kully,x):
    l=0
    u=len(kully)-1

    while l<=u:
        mid = (l+u)//2
        if kully[mid]==x:
            print("great its found")
            globals()['pos']=mid
            return True
        else:
            if kully[mid]<x:
                l=mid+1
            else:
                u=mid-1
    return False



kully=[23,27,29,30,32,36,40,54,64,68,70]
x=100
if search(kully,x):
    print("element is existed",pos+1)
else:
    print("element is not found")