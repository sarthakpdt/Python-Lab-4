num=int(input("enter a number:"))
k=0
if num==1:
    print("the number is nor prime nor composite")
elif num<0:
    print("invalid number")
else:
    i=2
    while i<num:
        if num%i==0:
            k=k+1
        i+=1
if k==0:
    print(num,"is a prime number")
else:
    print(num,"is not a prime number")
