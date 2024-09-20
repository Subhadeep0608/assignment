def min_distance(num1, num2):
    
    num1 = str(num1)
    num2 = str(num2)
    
    
    if len(num1) != len(num2):
        print("ERROR::Distance NA: Numbers must have the same number of digits")
        return
    
   
    min =None
    digits = None

    
    for i in range(len(num1)):
        digit1=num1[i]
        digit2=num2[i]
        distance = abs(int(digit1) - int(digit2))

       
        if (min is None or distance < min):
            min = distance
            digits = (digit1, digit2)
    
    
    if min is not None:
        print(f"Distance {min}, Digits are {digits[0]} and {digits[1]}")
    else:
        print("Distance NA: No corresponding digits found")


min_distance(52782, 39320)