def supername(name_1,name_2):
    sum_1=0
    sum_2=0
    for i in range(0,len(name_1)):
        sum_1=sum_1+ord(name_1[i])

    for i in range(0,len(name_2)):
        sum_2=sum_2+ord(name_2[i])

    if(sum_1==sum_2):
        if(name_1==name_2):
            print("both names are same")
        else:
            print("both names are different but same ascii value")
    elif(sum_1>sum_2):
        return name_1
    else:
        return name_2
    

print("enter 2 names of same lenth")
name_1=input()
name_2=input()
if(len(name_1)==len(name_2)):
    print("the supername is ",supername(name_1,name_2))

else:
    print("names are not of same length,try again")