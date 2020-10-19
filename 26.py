print(0o55)
print(0xf)
# logical operations
v=6
b=10
print(b>11 and v<7) # b>11 false(0),v<7 True(1) = 0  (0x1)=0
print(b<11 and v<7)
print(b>45 or v==6) # b>45 false(0),v==6 true(1)     0+1=1 hence answer is true
### bit wise operation AND-&, OR-| ,XOR-^, compliment ~(tilde), not-not. these are the simbols which we can use for bitwise operations.
print(12 & 13) # 1100(12) & 1101(13) just perform AND bitwise operations u will get 1100(12)
print(12 | 13) # 1100(12) & 1101(13) just perform OR bitwise operations u will get 1100(13)
print(12 ^ 13) # 1100(12) & 1101(13) just perform XOR bitwise operations u will get 0001(1)
#unary operation
n=7
print(n)     
n=-n
print(n)
# left shift and write shift
# left shift and write shift
print(1010 << 2)   #101000   1010.00 = 101000
print (1010 >> 2)    #1010   1010  =10.10
print (0b101000)
print(~1010)
print(5 and 7)  # Actually, ‘and’ sees the value on the left. If it has a True Boolean value, it returns whatever value is on the right. Otherwise, it returns False. So, here, 5 and 7 is the same as True and 7. Hence, it returns 7. However, 5&7 is the same as 101&111. This results in 101, which is binary for 5.

x=int(input("enter the value"))
y=int(input("enter the 2nd value"))
f=x+y
print(f)

x=eval(input("enter the numbers")) # eval will be used when we want to to some expre math ex.2+4-4
print(x)
# below code is for getting first characyer of the string
y=input(("enter the name"))
print(y[0])

h=input("enter the name ")[0]
print(h)
