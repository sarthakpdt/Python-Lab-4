sen=str(input("enter the sentence:"))
lower=0
upper=0
digit=0
sc=0
i=1
while i<len(sen):
    if (sen[i]>="a" and sen[i]<="z"):
        lower+=1
    elif (sen[i]>="A" and sen[i]<="Z"):
        upper+=1
    elif (sen[i]>="0" and sen[i]<="9"):
        digit+=1
    else:
         sc+=1
    i+=1
print("total number of lowercase letters are:",lower)
print("total number of uppercase letters are:",upper)
print("total number of digits letters are:",digit)
print("total number of special character letters are:",sc)

