#lab6_p6.py

#함수안에 함수를 정의 count_digit이라는 개미수열의 다음항 출력하는 함수 형성
def lookAndSay(n, i):
    def count_digits(number):
        # 입력받은 숫자를 문자열로 변환
        number_str = str(number)

        # 각 숫자가 몇 번 등장했는지를 저장할 딕셔너리 초기화
        digit_counts = {}

        # 각 숫자가 몇 번 등장했는지 계산
        for digit in number_str:
            if digit in digit_counts: #이미 앞서서 등장했던 숫자면
                digit_counts[digit] += 1
            else: #새로 등장하는 숫자의 경우 일단 1 추가하고 뒤에 위의 if이용해서 추가 count
                digit_counts[digit] = 1

        # 결과 문자열 생성
        result = ''
        for digit in sorted(digit_counts.keys()):
            count = digit_counts[digit]
            result += f"{count}{digit}"

        return int(result) #결과 return int형식으로

    #초기값 설정
    return_list = [n]
    return_boolean = False

    #이미 list에 1개 추가했으므로 n-1개의 항만 더 추가
    for k in range(i-1):
        return_list.append(count_digits(return_list[-1]))

    #cycle 도달했는지 유무 return 판단
    if count_digits(return_list[-1]) == return_list[-1]:
        return_boolean = True

    return return_list, return_boolean



