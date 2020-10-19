# this program is on file reading concept using readline and readlines method

goal=open("fist.txt")
#print(goal.read())
#print(goal.readline(4))

#line=goal.readline()
#while line!="":
 #   print(line,end="")
  #  line=goal.readline()

# by using readlines method we can
for line in goal.readlines():
    print(line,end="")
