#lab4_p3.py

#input받는 구문
num = input("Enter a number: ") #type = string

#0만 따로 생각
if num == '0': #type이 string 이므로 0으로 표시
    print('The number 0 contains 1 digit')
else:
    digits = len(num) #string 자리수 세기
    print('The number', num, 'contains', digits,'digits')