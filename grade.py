grade = 85

if grade >=60:
    print('passed')
    print('You have done a good job')
if grade <=60:
   print('failed')
   print('You need to work more on your self')

grade = 60

if grade>=55 :
  result = 'Passed'
  print( result)
else:
  result = 'failed'
  print(result,'You must take this course AGAIN!!!')

print('Passed' if grade>=55 else 'failed')

if 1:
  print('Nonzero value are not true, so this will print')
if 0:
  print('zero are false, so this will not print')