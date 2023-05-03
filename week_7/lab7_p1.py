#lab7_p1.py

def resetValuesInPlace(L, threshold):
    '''
    list인자 내에 threshold를 넘는 값을 0으로 바꿔 list를 return한다
    :param L: input되는 list
    :param threshold: L 인자내에 0으로 바꿀 수의 한계값
    :return: 바뀐 L
    '''
    for k in range(0, len(L)): #loop 설정을 통해 반복
        if L[k] > threshold:
            L[k] = 0
    return L

