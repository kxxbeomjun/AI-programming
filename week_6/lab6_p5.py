#lab6_p5.py
#factorial 함수를 위해 import
from math import factorial

#exp함수: 만들기 m을 집어넣어 n번째 항까지 출력해주는 함수
def exp(m, n):
    m = float(m)
    result = 1
    for i in range(1, n+1):
        result += m ** i / factorial(i)

    return format(result, '.6f') #6digit까지만 출력해주는 함수

#cos함수 정의, exp함수와 비슷한 형태
def cos(m, n):
    m = float(m)
    result = 1
    sign = -1
    for i in range(2, 2*n-1, 2):
        result += sign * m ** i / factorial(i)
        sign *= -1 #플러스 마이너스를 계속해서 바꿔주는 형태
    return format(result, '.6f') #6digit까지만 출력해주는 함수

#sin 함수 정의
def sin(m, n):
    m = float(m)
    result = 0
    sign = 1
    for i in range(1, 2*n, 2):
        result += sign * m ** i / factorial(i)
        sign *= -1 #플러스 마이너스를 계속해서 바꿔주는 형태
    return format(result, '.6f') #6digit까지만 출력해주는 함수

#getting input & boolean flag
quit_exit = False

#input을 계속 받을 수 있는 loop를 구성
while not quit_exit:
    A = input('Evaluate the equation: ')
    if A == '0': #0을 입력하면 escape
        quit_exit = True
    else:
        func, a, b = A.split()
        a = format(float(a), '.4f')  # 4 digit으로 변경
        b = int(b)

        # print 구문
        if func == 'exp':
            print(f"Using {b} term(s), exp({a}) is {exp(a, b)}")
        elif func == 'cos':
            print(f"Using {b} term(s), exp({a}) is {cos(a, b)}")
        elif func == 'sin':
            print(f"Using {b} term(s), exp({a}) is {sin(a, b)}")