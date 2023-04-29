#lab5_p1.py

#boolean flag
pos_num = False
max_num = 0

#While loop 이용
while not pos_num:
    num = float(input('Enter a number: '))
    if num > 0:
        if max_num < num: #더 largest number을 저장하는 방법
            max_num = num
    else:
        pos_num = True

#두가지 경우 나눠서 print
if max_num == 0:
    print('No positive number was entered')
else:
    print('The largest number entered was', format(max_num, '.2f')) #소숫점 두자리
