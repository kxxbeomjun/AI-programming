#lab8_p6.py

def getFile():
    """
    파일이름을 input으로 받고, 받은 input을 열어서 input_file로 return한다.
    learn us에 올라온 open source를 그대로 사용했다.
    """
    input_file_opened = False
    while not input_file_opened:

        #try-except 구문
        try:
            file_name = input('Enter input file name (with extension): ')
            input_file = open(file_name, 'r')
            input_file_opened = True
        except OSError:
            print ('Unable to open input file, please reenter')
    return file_name, input_file

def countWords(file_name):
    """
    파일을 새로 열어서 word들을 count하고 .wc확장자 파일에 write한다
    각 단어는 다 소문자로 바꾸고, sort하여 write한다.
    """
    cnt = {}

    with open(file_name, 'r') as f1:
        #얼마나 자주 등장하는지 찾기 위해 첫 index부터 cnt
        for line in f1:

            #소문자로 바꾸고 strip, split해서 단어별로 나눈다.
            words = line.strip().lower().split()
            for word in words:
                #이미 있는 단어면 cnt 1올리기
                if word in cnt:
                    cnt[word] += 1

                #없었으면 새로 만들어서 1저장
                else:
                    cnt[word] = 1

    #cnt에 저장된 단어를 sort
    word_sorted = sorted(cnt.items())

    #output 파일은 확장자 .wc로 변경하기
    output = file_name.replace('.txt', '.wc')


    with open(output, 'w') as file:
        #sort된 단어들에서 f-string이용해서 write
        for word, count in word_sorted:
            file.write(f"{word}: {count}\n")

file_name, input_file = getFile()
countWords(file_name)
