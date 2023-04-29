#lab6_p4.py

fruits = [] #빈 list 형성
while True: #while loop 형성
    fruit_name = input("Enter a fruit type (q to quit): ")
    if fruit_name == 'q': #escape 구문
        break
    weight = int(input("Enter the weight in kg: "))
    found = False
    for i in range(len(fruits)):
        if fruits[i][0] == fruit_name: #sublist 앞에는 과일이름
            fruits[i][1] += weight #뒤에는 무게를 저장(누적해서)
            found = True
            break
    if not found:
        fruits.append([fruit_name, weight]) #list에 새로 append
fruits.sort(key=lambda x: x[0]) #사전식으로 sorting

if fruits == []: #입력된게 없을 때 예외처리
    print("No data received, exiting.")
else:
    for fruit in fruits:
        print(f"{fruit[0]}, {fruit[1]}kg.") #fstring 이용해서 출력