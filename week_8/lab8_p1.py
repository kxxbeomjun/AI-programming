#lab8_p1.py

def countLetters(line):
    """
    Counting all letter characters in string "line"
    and write the result to file "answer.txt"

    The number of letter characteres must be written to the file:
    :param line: 입력되는 값
    :return:
    """

    count = 0 #letter의 count 수
    for k in line:
        if k.isalpha():
            count += 1

    with open('answer.txt', 'w') as file:
        file.write(str(count) + '\n') #string으로 변환