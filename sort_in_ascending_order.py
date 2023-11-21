number1 = float(input('Enter A Decimal Number: '))
number2 = float(input('Enter Another Decimal Number: '))
number3 = float(input('Enter Another Decimal Number: '))

if number1>number2 and number2>number3:
	print(number3,' ',number2,' ',number1)
if number2> number1 and number1>number3:
	print(number3,' ',number1,' ',number2)
if number3>number2 and number2>number1:
	print(number1,' ',number2,' ',number3)