def factorial(n):
    fact=1
    if(n==0 or n==1):
        return 1
    
    while(n>=1):
        fact=fact*n
        n-=1
    return fact


n=int(input("enter the number: "))
sum=0
c=n
while(n>0):
    r=n%10
    fact=factorial(int(r))
    sum=sum+(fact)
    n//=10

if(c==sum):
    print("its a strong number")
else:
    print("its not a strong number")