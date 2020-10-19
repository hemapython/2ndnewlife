#next program for selection sort
#in selection sort we will just pick one element and keep on continue to compare that value with other elements according the condition, untill we get list in sorted way
def sort(priya):
    for i in range(0, len(priya)-1,1):
        minpos=i
        for j in range(i):
            if priya[j]<priya[minpos]:
                minpos=j
                temp=priya[i]
                priya[i]=priya[minpos]
                priya[minpos]=temp

priya=[45,2,12,56,34,98,45,22,11,90,32,67]
sort(priya)
print(priya)

