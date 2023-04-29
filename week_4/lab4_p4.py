#lab4_p4.py

#num = 1 정의해서 1씩 키워나감
num = 1
for i in range(10): #10개마다 line change 하니깐 10번
    for j in range(10):
       print(format(num, '>3'), end="") #3자리수 오른쪽 정렬
       num += 1
    print("\n") # 라인 change

