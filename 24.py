# write a program for selection sort for ascending order with deatils ---
# " detailed decription i hav ereturned in book please refer the  same
def sort(dog):
    for i in range(5):
        min=i
        # every time j's loop will get start based on i loop
        for j in range(i,5):
            if dog[j] < dog[min]:
                min = j
        temp = dog[i]
        dog[i] = dog[min]
        dog[min] = temp

        print(dog)

dog=[45,16,20,4,8,35]
sort(dog)
print(dog)