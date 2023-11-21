total_grade=0
grade_counter = 0
grades = [98,76,71,87,83,90,57,79,82,94]

for grade in grades:
  total_grade +=grade
  grade_counter+=1

average = total_grade/grade_counter
print(f"The Average Grade Of The Class is {average} ")