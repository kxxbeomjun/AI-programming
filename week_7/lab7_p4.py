#lab7_p4.py

def evalPolynomial(x ,L):
    '''
    list의 인자를 다항식의 개수로 갖는 다항식을 만들어 x를 대입한 값을 return한다.
    :param x: 다항식에 입력할 x값
    :param L: 다항식의 개수를 인자로 갖는 list
    :return: 다항식에 x를 넣어 계산한 값
    '''
    result = 0
    for i, k in enumerate(L): #index와 value를 둘다 가져올 수 있는 method 사용
        result += k * x**i
    return result
