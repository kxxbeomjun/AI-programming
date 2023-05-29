"""
Name : Beomjun Kim
Student ID : 2017144078
Lab problem : lab9_p4.py
"""

class Fraction(object):
    """
    분수로 만들어주는 작업들이 포함된 함수들을 모은 class
    """

    def __init__(self, n, d):
        """
        분모, 분자를 받고 분자, 분모가 int 가 아닌 경우와 분모가 0인 경우 error문 발생
        """
        if type(n) != int or type(d) != int:
            raise ValueError('requires type int')
        if d == 0:
            raise ZeroDivisionError('requires non-zero denominator')

        #n,d값을 저장
        self.num = n
        self.denom = d
        self.reduce()

    def __str__(self):
        """
        분자/분모로 표현한 것을 return해주는 함수
        """
        return str(self.num) + '/' + str(self.denom)

    def __mul__(self, other):
        """
        self * other한 값을 return해주는 함수
        """
        new_num = self.num * other.num
        new_denom = self.denom * other.denom
        return Fraction(new_num, new_denom)

    def __add__(self, other):
        """
        self + other한 값을 return해주는 함수
        """
        new_num = self.num * other.denom + other.num * self.denom
        new_denom = self.denom * other.denom
        return Fraction(new_num, new_denom)

    def __float__(self):
        """
        float-value를 return해주는 함수
        """
        return self.num / self.denom

    def gcd(self, a, b):
        """
        아래 reduce함수에서 사용할 최대공약수 생성 유클리드 알고리즘
        """
        while b != 0:
            a, b = b, a % b
        return a

    def reduce(self):
        """
        분자, 분모를 최대공약수로 나눠서 표현해주는 함수
        """
        common = self.gcd(abs(self.num), abs(self.denom))

        if self.num < 0 and self.denom < 0:
            self.num, self.denom = abs(self.num), abs(self.denom)

        #다시 분모, 분자 저장
        self.num //= common
        self.denom //= common

    def adjust(self, factor):
        """
        분모, 분자에 factor을 곱하는 함수
        """
        self.num *= factor
        self.denom *= factor

