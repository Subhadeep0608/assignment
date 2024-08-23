n=int(input("enter the range of the series : "))
a=0
b=1
print("The fibonnacci series is as follows:-")
print(a,end=" ")
print(b,end=" ")

for i in range (1,n-1):
    s=a+b
    print(s,end=" ")
    a=b
    b=s