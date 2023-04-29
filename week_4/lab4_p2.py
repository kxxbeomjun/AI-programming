#lab4_p2.py

#input받는 구문 while loop 이용
#boolean flag 이용
zero = False
#개수 세기 위한 parameter
positive_num = 0
negative_num = 0

while not zero:
    num = int(input('Your number: '))
    if num == 0: #0 입력시 loop escape
        zero = True
    elif 0 < num < 100: #100 이상은 count 하지 않는다
        positive_num += 1
    elif num < 0:
        negative_num += 1

#print 구문
print('Positive values:', positive_num)
print('Negative values:', negative_num)