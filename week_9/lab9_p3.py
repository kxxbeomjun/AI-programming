"""
Name : Beomjun Kim
Student ID : 2017144078
Lab problem : lab9_p3.py
"""

import random

def make_key():
    """
    랜덤 키를 만드는 함수 return으로는 만들어진 key를 저장
    """
    characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 '
    random_characters = random.sample(characters, len(characters))
    key_dict = {} #최종 key를 저장할 dict

    # for루프를 사용해서 characters와 random_characters의 각 원소를 하나씩 가져와서 새로운 딕셔너리 key_dict에 추가
    for i in range(len(characters)):
        key_dict[characters[i]] = random_characters[i]
    return key_dict


def encrypting_n_decrypting(input, key, mode):
    """
    암호화하거나 복호화하는 함수
    암호/복호화한 결과를 return한다.
    """
    output = ''
    for char in input:
        if char == '\n': #개행문자는 그대로 사용해도된다.
            output += char
            continue

        if mode == 'encrypt': #암호화인 경우
            output += key.get(char, char)
        else: #복호화인 경우
            for original, encrypted in key.items():
                if encrypted == char:
                    output += original #복호화된 글을 ouput에 넣기
                    break
    return output

def main():
    """
    main함수: 파일명을 input받아, 어떤 확장자인지 판단하고 각각 경우의 과정을 진행한다.
    """
    filename = input('Enter a filename: ')
    split_name = filename.rsplit('.', 1) #"."을 기준으로 문자열을 두개로 나눠서 txt인지 enc인지 확인
    base_name = split_name[0]
    ext = '.' + split_name[1] if len(split_name) > 1 else '' #확장자가 없는 파일일 수도 있으므로

    #try-except를 통해서 존재하지 않는 파일명의 경우 terminate
    try:
        with open(filename, 'r') as file:
            content = file.read()
    except FileNotFoundError:
        print('Cannot find the file.')
        return

    # txt확장자의 경우 = 암호화
    if ext == '.txt':
        key = make_key() #새로운 key를 만들어야하므로 make_key함수를 실행

        # ".key" 확장자 파일을 만든다.
        with open(base_name + '.key', 'w') as file:
            file.write(str(key))
        encrypted = encrypting_n_decrypting(content, key, 'encrypt')

        #".enc"파일 확장자를 만든다.
        with open(base_name + '.enc', 'w') as file:
            file.write(encrypted)
        #여기까지하면 암호화 완료, 키는 .key 파일에 저장된다.

    #".enc"확장자의 경우 = 복호화
    elif ext == '.enc':

        #주어진 ".key" 파일을 열어본다.
        try:
            with open(base_name + '.key', 'r') as file:
                key = eval(file.read())

        #key 파일이 없으면 terminate
        except FileNotFoundError:
            print('Cannot find the key file.')
            return

        #복호화하는 경우
        decrypted = encrypting_n_decrypting(content, key, 'decrypt')

        #".txt"파일을 만들어서 복호화된 내용을 쓴다.
        with open(base_name + '.txt', 'w') as file:
            file.write(decrypted)
        #여기까지하면 복호화 완료

    #만약 ".enc"확장자 이름의 파일이 없으면 terminate
    else:
        print('Cannot find the file.')

if __name__ == "__main__":
    main()

