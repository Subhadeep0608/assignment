def check_prime(n):
    if(n==2):
        return True
    elif(n==0 or n==1):
        return False
    else:
        for i in range(2,(int(n**0.5))+1):
            if(n%i==0):
                return False
        return True


n= int(input("enter the number: "))
print(f"the given number is prime? \n {check_prime(n)}")