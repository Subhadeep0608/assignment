def num_to_words(n):
    ones = ['', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine']
    teens = ['Ten', 'Eleven', 'Twelve', 'Thirteen', 'Fourteen', 'Fifteen', 'Sixteen', 'Seventeen', 'Eighteen', 'Nineteen']
    tens = ['', '', 'Twenty', 'Thirty', 'Forty', 'Fifty', 'Sixty', 'Seventy', 'Eighty', 'Ninety']
    notation = ['', 'Thousand', 'Million', 'Billion','trillion']

    def converter(num):
        if num < 10:
            return ones[num]
        elif num < 20:
            return teens[num-10]
        elif num < 100:
            return tens[num//10] + ('' if num%10==0 else ' ' + converter(num%10))
        elif num < 1000:
            return ones[num//100] + ' Hundred' + ('' if num%100==0 else ' and ' + converter(num%100))

    result = ''
    i = 0
    while n > 0:
        if (n % 1000 != 0):
            result = converter(n%1000) + ' ' + notation[i] + ' ' + result
        n //= 1000
        i += 1
    return result.strip()



n=int(input("enter our number: "))
print(num_to_words(n)) 


