num=[]
for i in range(1,5):
    n= int(input("enter the number: "))
    num.append(n)

max=num[0]
min=num[0]

for i in range (1,4):
    if(num[i]>max):
        max=num[i]
    if(num[i]<min):
        min=num[i]


print(f"the maximum number among them is{max}")
print(f"the minimum number among them is{min}")

# print(f"the maximum number among them is{max(num)}")
# print(f"the minimum number among them is{min(num)}")