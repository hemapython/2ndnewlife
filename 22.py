# write a program for ascending order using selectin sort.
def sort(pen):
    for i in range(0,len(pen)-1,1):
        min=i
        for j in range(i,len(pen)): # or u can give total length of list because in next insruction j will compare with j itself so one count needs to be added here in order to get the loop count
            if pen[j] < pen[min]:
             min = j

        temp= pen[i]
        pen[i]=pen[min]
        pen[min]=temp

        print(pen)

pen = [56,26,75,16,11,21,4,45,23,77,55,33]
sort(pen)

print(pen)