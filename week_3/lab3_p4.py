#lab3_p4.py

import datetime

#Get month, day, year of birth of person 1
month_birth_1 = int(input('Person 1: Enter month born (1-12): '))
day_birth_1 = int(input('Person 1: Enter day born (1-31): '))
year_birth_1 = int(input('Person 1: Enter year born (4-digit): '))

#Get month, day, year of birth of person 2
month_birth_2 = int(input('Person 2: Enter month born (1-12): '))
day_birth_2 = int(input('Person 2: Enter day born (1-31): '))
year_birth_2 = int(input('Person 2: Enter year born (4-digit): '))

#Get month, day, year of birth
current_month = datetime.date.today().month
current_day = datetime.date.today().day
current_year = datetime.date.today().year

#Determine number of seconds in a day
numsecs_day = 24 * 60 * 60
numsecs_year = 365 * numsecs_day

avg_numsecs_year = ((4 * numsecs_year) + numsecs_day) // 4
avg_numsecs_month = avg_numsecs_year // 12

#Calculate approximate age in seconds of person 1,2
numsecs_1900_bod1 = ((year_birth_1 - 1900) * avg_numsecs_year) + \
                    ((month_birth_1 - 1) * avg_numsecs_month) + \
                    (day_birth_1 * numsecs_day)

numsecs_1900_bod2 = ((year_birth_2 - 1900) * avg_numsecs_year) + \
                    ((month_birth_2 - 1) * avg_numsecs_month) + \
                    (day_birth_2 * numsecs_day)

#절댓값으로 계산한 값 출력
age_difference = abs(numsecs_1900_bod1 - numsecs_1900_bod2)
print('Age difference in seconds:', age_difference)