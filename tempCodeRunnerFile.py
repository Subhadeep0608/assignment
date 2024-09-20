def converter_in(num):
#     if num<10:
#         return ones[num]
#     elif num<20:
#         return teens[num-10]
#     elif num<100:
#         return tens[num//10]+(''if num%10==0 else ''+converter_in(num%10))
#     elif num<1000:
#         return ones[num//100] + 'Hundred'+(''if n%100==0 else 'and '+ converter_in(num%100))

#   def converter(num):
#         if num < 10:
#             return ones[num]
#         elif num < 20:
#             return teens[num-10]
#         elif num < 100:
#             return tens[num//10] + ('' if num%10==0 else ' ' + converter(num%10))
#         elif num < 1000:
#             return ones[num//100] + ' Hundred' + ('' if num%100==0 else ' and ' + converter(num%100))



# result=''
# i=1
# while(n>0):
#     if(n%1000!=0):
#         result= converter(n%1000)+' '+ notation[i]+ result

