age = int(input('Enter Your Age: '))

maximum_heart_rate = 222-age
max_target_heart_rate = maximum_heart_rate*(85/100)
min_target_heart_rate = maximum_heart_rate*(50/100)

print('Your maximum heart rate is ',maximum_heart_rate)
print('Your maximum Target heart rate is ',max_target_heart_rate)
print('Your minimum Target heart rate is ',min_target_heart_rate)

