"""
Name : Beomjun Kim
Student ID : 2017144078
Lab problem : lab9_p1.py
"""

def addDailyTemp(mydict, day, temperature):
    """
    Add key 'day' and value 'temperature' to the dictionary 'mydict',
    day의 key가 존재하지 않는 경우만 추가
    return: mydict
    """
    if day not in mydict: #존재하지 않는 경우만 dictionary에 추가
        mydict[day] = temperature
    return mydict
