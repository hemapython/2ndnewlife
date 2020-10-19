
  # index starts from 0 but length = no. of elements but 1 has to sustitute in order to obtain max index number
def sort(dummu):
      #loop will start from max index and will end at 0, -1 <<---  right to left
    for i in range(len(dummu)-1, 0 , -1):
        # here i is becoz in every iteration of j, only index number values will get swap and the resr remains same so hence typing index numbers
        # in place of i is waste of time
        for j in range(11):
            # here < or > this symbol indicates ascending or descending order
            # in this pgm j will  start from o index numbers only. regardless of direction of i it means left to right or right to left
            if dummu[j] > dummu[j+1]:
                temp=dummu[j]
                dummu[j]=dummu[j+1]
                dummu[j+1]=temp

dummu=[34,56,2,55,90,34,23,63,68,21,56,34]
# here sort is not inbuilt function hence has to create the 'sort method'
sort(dummu)
print(dummu)


#combu=[56,34,28,56,22,9,17,55,45,39]
#combu.sort(reverse=True)
#print(combu)


