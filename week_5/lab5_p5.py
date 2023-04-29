#lab5_p5.py
#list를 사용해야함

#boolean flag
loop_escape = False
list =[] #빈 리스트

while not loop_escape:
    name = input('Enter a name (q to quit): ')
    if name == 'q': #q를 눌러 quit 구문
        loop_escape = True
    else:
        list.append(name)

a_count = 0 #a를 세기 위한 파라미터

for k in list:
    for m in k:
        if m.lower() == 'a':
            a_count += 1

#print구문
print("Appearance of letter 'a':", a_count)
