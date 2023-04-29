#lab6_p3.py

#boolean flag & making list
quit_exit = False
word_list = []

#input을 반복적으로 받는 경우
while not quit_exit:
    word = input('Enter a word (q to quit): ')

    #exit 구문
    if word == 'q':
        quit_exit = True
    # 첫번째문자가 반복되는지 판단하는 구문
    else:
        word_lower = word.lower()
        if word_lower[0] in word_lower[1:]:
            if word in word_list:
                pass
            else: #list안에 없는 문자일 경우만 append
                word_list.append(word)

#list내에 문자들을 사전식으로 정렬하는 method
word_list.sort()
print(word_list)