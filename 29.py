#"For" loop example
#for i in range(51,31,-1):
 #  if i%5!=0:
  #    print(i)

# demonstrating "continue" key word
av=5
x=int(input("enter the number"))

i=1
while i<=x:
   if av>i:
      print("candy is out of stock")
      break

   print("candy")
   i+=1


# continue statement
for i in ("red","orange","yello","pink","safron"):
   if i=="yello":
      continue # all the index values will get iterate one by one , but once loop (index value) reaches yello element in the
      # list loop directly goes to next iteration instead of executing next statement in the loop block.
   print(i)
print("the end  ") # this statement is supposed to be execute once loop has finished it iterations

# break statement
for i in ("red","orange","yellow","pink","safron"):
   if i=="pink":
      break # once i value is equal to pink it just make loop to come out of it , and next statement will get execute here(the end)
   print(i)
print("the end")

for i in range(4):
   for j in range(4): # for reverse (4-i)
      print("#",end="")
   print()







