number = int(input('Enter five digit number'))

if  number>=100000:
    print('INVALID NUMBER')

first_digit = number//10000
remainder = number%10000
second_digit = remainder//1000
remainder1 = remainder%1000
third_digit = remainder1//100
remainder2 = remainder1%100
forth_digit = remainder2//10
fifth_digit = remainder%10

print(first_digit,'  ',second_digit,'  ',third_digit,'  ',forth_digit,'  ',fifth_digit)