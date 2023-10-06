# def ExchangeDollarToKhmer(number):
#     numberchange = number*4000
#     return numberchange
# dollar = int(input())
# change = ExchangeDollarToKhmer(dollar)8
# print(change)



# def rectangle(number):
#     valueX = ""
#     for i in range(number):
#         for i in range(1):
#             valueX += number * 'X'
#         valueX += '\n' 
#     return valueX

# addX = int(input())
# Enter = rectangle(addX)
# print(Enter)




# def countLetterX(string):
#     hasX = 0
#     for i in string:
#         if (i == 'X' or i == 'x'):
#             hasX += 1
#     return hasX
# textInput = str(input())
# result = countLetterX(textInput)
# print(result)


def sum(value1,value2):
   return value1+value2
start = int(input())
end = int(input())
total = 0
for i in range(start,end+1):
      if start > end:
         total =0
      else:
         total += i
value1 = total
value2 = 0
print(sum(value1, value2))


