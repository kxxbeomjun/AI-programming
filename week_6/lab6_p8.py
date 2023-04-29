#return boolean flag + print

def treePrinter(list_tree):
    isfullbinary = False #return의 default 값
    if len(list_tree) % 2 == 0:
        isfullbinary = False #len이 짝수면 마지막이 child node가 혼자다
    else: #root node 빼고 뒤를 두개씩 엮었을때 [x,y] subnode안에 x,y 중 한개만 None 이면 fullbinary X
        list_tree_couple = [list_tree[i:i+2] for i in range(1, len(list_tree), 2)]
        for k in range(len(list_tree_couple)):
            if list_tree_couple[k][0] == None and list_tree_couple[k][1] != None:
                isfullbinary = False
                break #하나라도 예외 발견하면 loop escape
            elif list_tree_couple[k][1] == None and list_tree_couple[k][0] != None:
                isfullbinary = False
                break #하나라도 예외 발견하면 loop escape
            else:
                isfullbinary = True

    if len(list_tree) == 1: #list의 범위에 따라서 함수를 나눔
        print(list_tree[0])

    elif len(list_tree) <= 3:
        list_tree = [' ' if element is None else element for element in list_tree] #none -> space 로
        list_tree = list(map(str, list_tree)) #합성을 위해서 모든인자를 str로
        list_tree_1 = list_tree[0:1] #리스트를 범위에 따라 끊었다.
        list_tree_2 = list_tree[1:len(list_tree)] #마지막 줄은 len를 통해 입력된 길이 까지만 출력되게 했다.
        list_tree_2 = " ".join(list_tree_2) #join함수를 통해서 2번째열어 출력되는 함수를 합성
        print(list_tree_1[0])
        print(list_tree_2)


    elif len(list_tree) <=7:
        list_tree = [' ' if element is None else element for element in list_tree]
        list_tree = list(map(str, list_tree))
        list_tree_1 = list_tree[0:1]
        list_tree_2 = list_tree[1:3]
        list_tree_2 = "   ".join(list_tree_2) #3칸 띄우고 2번째 줄 합성
        list_tree_3 = list_tree[3:len(list_tree)]
        list_tree_3 = " ".join(list_tree_3) #1칸 띄우고 3번째 줄 합성
        print(list_tree_1[0])
        print(list_tree_2)
        print(list_tree_3)

    elif len(list_tree) <= 15:
        list_tree = [' ' if element is None else element for element in list_tree]
        list_tree = list(map(str, list_tree))
        list_tree_1 = list_tree[0:1]
        list_tree_2 = list_tree[1:3]
        list_tree_2 = "       ".join(list_tree_2) #7칸 띄고 2번째 줄 합성
        list_tree_3 = list_tree[3:7]
        list_tree_3 = "   ".join(list_tree_3) #3칸 띄고 3번째 줄 합성
        list_tree_4 = list_tree[7:len(list_tree)]
        list_tree_4 = " ".join(list_tree_4) #한칸 띄고 1번째 줄 합성
        print(list_tree_1[0])
        print(list_tree_2)
        print(list_tree_3)
        print(list_tree_4)

    return isfullbinary
