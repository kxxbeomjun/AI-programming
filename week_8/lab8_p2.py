#lab8_p2.py


def copyFiles(f1, f2, f3):
    """
    copies the text of f1, f2 to f3
    :param f1: reading txt
    :param f2: reading txt
    :param f3: writing txt
    :return:
    """
    #f1,f2는 open, f3는 write
    with open(f1, 'r') as file_1, open(f2, 'r') as file_2, open(f3, 'w') as file_3:

        #두 줄에 나눠서 더해야지만 "\n"같은 additional text가 추가되지 않는다.
        file_3.write(file_1.read())
        file_3.write(file_2.read())

    #always return 0
    return 0