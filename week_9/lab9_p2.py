"""
Name : Beomjun Kim
Student ID : 2017144078
Lab problem : lab9_p2.py
"""

def moderateDays(mydict):
    """
    mydict을 입력받고, return으로는 평균이 70~ 79인 값들만 return
    """
    answer = [] #결과를 저장할 list
    for day, temperature in mydict.items():
        if 70 < temperature < 79: #70, 79는 범위에 포함하지 않는다.
            answer.append(day)
    return answer

