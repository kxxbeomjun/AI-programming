#lab6_p1.py

#getting input & split by blank
name_first, name_last = input('Enter a first and last name: ').split()

#첫번째 문자만 그대로 
first_letter_of_first = name_first[0]

#print
print(name_last + ',', first_letter_of_first + '.')