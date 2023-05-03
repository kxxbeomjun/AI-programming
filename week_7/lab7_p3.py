#lab7_p3.py

def resetValues(L, threshold):
    '''
    list내에 threshold를 넘는 인자를 0으로 바꾸어 새롭게 저장한 list를 return한다
    :param L: input list
    :param threshold: 0으로 입력될 임계값
    :return: Result라는 new list
    '''
    Result = []
    for k in range(len(L)):
        if L[k] > threshold:
            Result.append(0) #threshold보다 크면 0 append
        else:
            Result.append(L[k]) #나머지는 원래 값 append
    return Result
