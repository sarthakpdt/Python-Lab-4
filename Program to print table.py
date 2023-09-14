num=int(input("enter a number:"))
i=1
if num<0:
    print("wrong number")

else:
    while i<=20:
        print(num,"x",i,"=",num*i)
        i+=1
