#lab8_p5.py

def smooth(input_file):
    """
    입력받은 파일을 열어서 읽고, 각각의 인접한 수들의 평균을 구해 list를 print한다.
    :param input_file: 내가 읽을 파일
    :return: 평균값을 나열한 list를 print
    """

    #input_file을 열고 read
    with open(input_file, 'r') as f1:
        basic = [int(k) for k in f1]

    #맨 앞과 맨 뒤에는 한개씩 더 붙이기
    extended = [basic[0]] + basic + [basic[-1]]

    #기본 smomthed list 설정
    smoothed = []
    for i in range(1, len(extended)-1):

        #3개씩 묶어서 평균내기
        average = (extended[i-1] + extended[i] + extended[i+1]) / 3

        #평균낸 값 append
        smoothed.append(average)

    #print 구문
    print(smoothed)


