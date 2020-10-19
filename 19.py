# write a program for sorting numbers in descending
# and ascending order using an bubble sort method(i took around one week to understand this concept)
def bubble_sort(nihan):
     for i in range(len(nihan)-1, 0, -1):
         for j in range(i):
             if nihan[j] > nihan[j+1]:
                 temp = nihan[j]
                 nihan[j]=nihan[j+1]
                 nihan[j+1]=temp

nihan=[24,56,89,56,12,90,55,80]
bubble_sort(nihan)
print(nihan)












