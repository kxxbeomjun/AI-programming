#lab3_p3.py

#random 모듈 사용
import random

#빈 로또 list 형성
lotto = []

#임의의 수 6개 선택
for k in range(6):
    lotto.append(random.randint(1,45))
 #type = list

#print를 list에서 각각 해야한다
print("Lotto numbers of the week:", lotto[0], lotto[1], lotto[2], lotto[3], lotto[4], lotto[5])
