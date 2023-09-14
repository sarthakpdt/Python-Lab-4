x=int(input("enter the number:"))
y=int(input("enter the number:"))
n=int(input("enter the number to be checked:"))
i=1+x
if x>=y:
    print("invalid number:")
else:
    while i<y:
        if i%n==0:
            print(i)
        i+=1
