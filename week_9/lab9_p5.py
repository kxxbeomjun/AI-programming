"""
Name : Beomjun Kim
Student ID : 2017144078
Lab problem : lab9_p5.py
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

        # n,d값을 저장
        self.num = n
        self.denom = d

    def __str__(self):
        """
        분자/분모로 표현한 것을 return해주는 함수
        """
        return str(self.num) + '/' + str(self.denom)

    def __mul__(self, other):
        """
        other이 int인지 Fraction인지 판단하고 각각의 경우에 필요한 작업 진행 후 return
        Fraction일 경우는 분모, 분자를 각각 곱해서 다시 return
        int인 경우는 numerator × other/denominator 값 return
        둘다 아닐 경우 error 구문
        """

        #파이썬 내장 함수 ininstance를 사용해서 other이 Fraction인 경우
        if isinstance(other, Fraction):
            new_num = self.num * other.num
            new_denom = self.denom * other.denom
            return Fraction(new_num, new_denom)

        #other이 int인 경우
        elif isinstance(other, int):
            new_num = self.num * other
            return Fraction(new_num, self.denom)

        #둘 다 아닐 경우 error
        else:
            raise ValueError

    def __add__(self, other):
        """
        other이 int인지 Fraction인지 판단하고 각각의 경우에 필요한 작업 진행 후 return
        Fraction일 경우는 분모, 분자를 각각 더해서 다시 return
        int인 경우는 numerator + (denominator × other)/denominator 값 return
        둘다 아닐 경우 error 구문
        """

        #other이 Fraction인 경우
        if isinstance(other, Fraction):
            new_num = self.num * other.denom + other.num * self.denom
            new_denom = self.denom * other.denom
            return Fraction(new_num, new_denom)

        # other이 int인 경우
        elif isinstance(other, int):
            new_num = self.num + self.denom * other
            return Fraction(new_num, self.denom)

        # 둘 다 아닐 경우 error
        else:
            raise ValueError

    def __float__(self):
        """
        float-value를 return해주는 함수
        """
        return self.num / self.denom
