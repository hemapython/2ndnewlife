# revision on bubble sort concept
def sort(don):
   for i in range(0,len(don)-1,1):
        for j in range(len(don)-1):
            if don[j] > don[j+1]:
                temp=don[j]
                don[j]=don[j+1]
                don[j+1]=temp

don=[78543,42,64,13,86,53,83,90,55,44,11]
sort(don)
print(don)




