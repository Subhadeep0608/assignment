def armstrong(n):
    sum=0
    c=len(str(n))
    while(n>0):
        r=n%10
        sum=sum+(int(r)**c)
        n/=10
    return sum

n= int(input("enter the number: "))
sum=armstrong(n)
if(n==sum):
    print("its a armstrong number")
else:
    print("its not a armstrong number")
