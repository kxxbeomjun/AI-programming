#lab8_p4.py

def countAllLetters(line):
    """
    line에 있는 letter의 개수를 count해서 return list에 return 한다.
    만약 line에 아무 letter가 없다면, return 빈 리스트
    :param line: count해야하는 line
    :return: count된 리스트
    """
    #count한 letter를 저장할 곳
    count = {}

    #line을 다 lower로 변경
    line_lower = line.lower()

    #맨 앞 index부터 따져보기
    for i in line_lower:

        #letter인지 따지기
        if i.isalpha():

            #letter인데, 이미 있으면 count 1 추가
            if i in count:
                count[i] += 1
            #letter인데, 없으면 새롭게 1정의
            else:
                count[i] = 1

    #sort해서 저장
    result = sorted([(a, b) for a, b in count.items()])
    return result

