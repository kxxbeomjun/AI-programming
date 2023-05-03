#lab7_p2.py

def removeValuesInPlace(L, threshold):
    '''
    list인자 내에 threshold를 넘는 값을 제거한 list를 return한다
    :param L: input list
    :param threshold: 제거할 임계값
    :return: 제거된 L
    '''
    L_copy = L[:] #원본 list를 복사해서 사용
    i = len(L_copy) - 1 #index를 역순으로 하면 index가 망가질일이 없다.
    while i >= 0:
        if L_copy[i] > threshold:
            del L_copy[i]
        i -= 1
    L = L_copy #copy한 list와 동일화
    return L
