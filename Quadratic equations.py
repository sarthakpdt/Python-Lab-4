num1=int(input("enter the coeffecient of x2:"))
num2=int(input("enter the coeffecient of x:"))
num3=int(input("enter the rest value:"))

d=(num2**2)-(4*num1*num3)

if d<0:
    print("no real roots")
elif d==0:
    x=((-num2)/(2*a))
    print("2 equal roots and they are:"x,x)
else:
    z= ((-num2)+(d**(1/2)))/(2*num1)
    y= ((-num2)-(d**(1/2)))/(2*num1)

    print("2 distinct roots and the roots are:",z,y)
