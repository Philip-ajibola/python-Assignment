name1 = input('Enter Your Name ')
name2 = input('Enter Your Name ')

num1 = int(input(name1+' Enter A Number 0'',''1 And 2 '))
num2 = int(input(name2+' Enter A Number 0'',''1 And 2 '))

scissors = 0
rock = 1
paper = 2


if num1==scissors and num2==scissors:
      print("It is A Draw Between", name1, "And", name2)

if num1==scissors and num2==rock:
      print(name2, "WON", name1, "!!!!")

if num1==scissors and num2==paper:
     print(name1," WON", name2, "!!!!")

if num1==rock and num2==scissors:
      print(name1, "WON", name2,"!!!!");

if num1==rock and num2==paper:
     print(name2, "WON", name1,"!!!!");

if num1==rock and num2==rock:
     print("It is A Draw Between", name1, "And", name2)

if num1==paper and num2==scissors:
     print(name2, "WIN", name2,"!!!!");

if num1==paper and num2==rock:
      print(name1, "WIN", name2, "!!!!");

if num1==paper and num2==paper:
     print("It is A Draw Between",name1, "And", name2)







