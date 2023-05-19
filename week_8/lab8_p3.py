#lab8_p3.py

def copyFiles(f1, f2, f3):
    """
    copies the text of f1, f2 to f3
    but, handling the exception that if f1,f2 or f3 cannot be opened,
    return -1

    otherwise, copy and return 0

    :param f1: reading txt
    :param f2: reading txt
    :param f3: writing txt
    :return:
    """
    #try - except 구문을 통해서 예외처리
    try:
        with open(f1, 'r') as file_1, open(f2, 'r') as file_2, open(f3, 'w') as file_3:

            #역시나 2번 문제처럼, 각각 따로 write하여 구분
            file_3.write(file_1.read())
            file_3.write(file_2.read())

    #OSError 발생시 return -1
    except OSError:
        return -1

    #정상 작동하면 return 0
    else:
        return 0