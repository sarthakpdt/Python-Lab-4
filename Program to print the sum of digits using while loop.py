num=int(input("enter the number:"))
a=0
b=0
if num<0:
    print("invalid number")
else:
    while num!=0:
        a=num%10
        b=a+b
        num=num//10
print("the sum of the digits is:",b)
