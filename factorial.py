def factorial(n):
    if(n==0 or n==1):
        return 1
    fact=n*factorial(n-1)
    return fact
    
n=int(input("enter a number :"))
f=factorial(n)
print(f"the factorial of {n}={f}")