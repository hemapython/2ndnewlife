
# write an program for decsecnding order using bubble sore method
def sort(gilly):
        for i in range (0, len(gilly)-1, 1):
         # no of elements = 12 , it has to done for 11 times for 12 elements becoz the 1 which is left out which is automatically at its position
         for j in range(len(gilly)-1):
            if gilly[j] < gilly[j+1]:
                    temp = gilly[j]
                    gilly[j]=gilly[j+1]
                    gilly[j+1]=temp

gilly=[75,34,23,1,2,67,54,33,90,23,56,65]
sort(gilly)
print(gilly)