
# write a program for descending order using an selection sort

def sort(ant):
      #for descending oder u have to from highest index to lowest index
    for i in range(6):
        maxpos = i
        for j in range(i,6):
              if ant[j] > ant[maxpos]:
                  maxpos = j

        temp = ant[i]
        ant[i] =ant[maxpos]
        ant[maxpos] = temp

        print(ant)

ant= [34,23,11,64,30,14,18]
sort(ant)
print(ant)











