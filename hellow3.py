x = int(input("enter the number"))
y = x % 2
if y == 0:
    print("number is even")
    if x > 4:
        print("its greater than x")
    else:
        print("its not greater than x")
else:
    print("number is odd")