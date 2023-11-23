number1 = int(input('Enter First Number: '))
number2 = int(input('Enter Second Number '))
number3 = int(input('Enter third Number '))

sum = number1 + number2 + number3
product = number1*number2*number3
average = sum/3

highest = 0
lowest = number1

if number1>highest:
   highest = number1
   
if number2>highest:
   highest = number2

if number1<lowest:
   lowest = number1


if number3>highest:
   highest = number3

if number1<lowest:
   lowest = number1

if number2<lowest:
   lowest = number2

if number3<lowest:
   lowest = number3
print(sum,'is the sum of the three number ')
print(product,'is the product of three number ')
print(average,'is the average of  three number ')
print(highest,'is the highest number')
print(lowest,'is the lowest  number')