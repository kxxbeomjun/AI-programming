#lab5_p4.py

#getting input
num = int(input('Enter an integer: '))

#역삼각형을 출력하는 함수를 구성
def print_triangle(n):
    for k in range(n, 0, -1):
        print(' '*(n-k) + '*'*(2*k-1))

#함수실행
print_triangle(num)