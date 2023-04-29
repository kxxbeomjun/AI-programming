#lab3_p2.py

#getting first 12th number
EAN = input("Enter the first 12 digits of an EAN: ")

#짝수합, 홀수합
even_sum = 0
odd_sum = 0

for k in range(len(EAN)):
    if k % 2 == 1: #파이썬은 두번째가 index 1
        even_sum += int(EAN[k])
    else:
        odd_sum += int(EAN[k])

#step 1~4
remainder = (even_sum * 3 + odd_sum) - 1

#step 5
remainder = remainder % 10

#step 6
check_digit = 9 - remainder

#print
print("Check digit:", check_digit)
