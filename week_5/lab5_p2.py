#lab5_p2.py

#getting input
input_sentence = input("Enter a sentence: ")

# "a, e, i, o, u" 모음 개수 세기
vowel_count = 0
for k in input_sentence:
    if k.lower() in "aeiou": #소문자로 바꿔서 대/소문자 둘다 count
        vowel_count += 1 #count 구문

#print 구문 1개 일 때 따로
if vowel_count == 1:
    print('Your sentence contains', vowel_count, 'vowel.')
else:
    print('Your sentence contains', vowel_count, 'vowels.')