#lab7_p7.py

import stack

#boolean flag
loop_escape = False

while not loop_escape:
    symbol = input('Enter an RPN expression: ')
    if symbol == 'q': #loop escape
        loop_escape = True
    else:
        mystack = stack.getStack() #blank list = [] 형성
        symbol = list(symbol.split()) #<class, 'list'>
        count_equal = symbol.count('=')

        if count_equal != 1: #'='가 여러개 or 안들어 있는 경우
            print('Evaluation error')
            break
        elif symbol[-1] != '=': #'='가 맨 끝에 위치하지 않는 경우
            print('Evaluation error')
            break

        for k in symbol:
            if k == '=':
                result = stack.pop(mystack)
                empty_check_after_result_pop = stack.isEmpty(mystack)
                if result == None or empty_check_after_result_pop == False: #stack not empty after '='
                    print('Evaluation error')
                    loop_escape = True #terminate the program
                    break
                else:
                    if "." in str(result): #float 타입이면 2digit까지 출력
                        print('Value of expression:', format(result, '.2f'))
                    else: #int형식이면 그대로 출력
                        print('Value of expression:', result)

            elif k == '+':
                popped_1 = stack.pop(mystack)
                popped_2 = stack.pop(mystack)
                if popped_1 == None or popped_2 == None: #연산자 둘 중 하나가 None 인 경우
                    print('Evaluation error')
                    loop_escape = True #terminate the program
                    break
                else:
                    plus_popped = popped_1 + popped_2 #더해서 push
                    stack.push(mystack, plus_popped)

            elif k == '*':
                popped_3 = stack.pop(mystack)
                popped_4 = stack.pop(mystack)
                if popped_3 == None or popped_4 == None: #연산자 둘 중 하나가 None 인 경우
                    print('Evaluation error')
                    loop_escape = True #terminate the program
                    break
                else:
                    multi_popped = popped_3 * popped_4 #곱해서 push
                    stack.push(mystack, multi_popped)

            elif k == '/':
                popped_5 = stack.pop(mystack)
                popped_6 = stack.pop(mystack)
                if popped_5 == None or popped_6 == None: #연산자 둘 중 하나가 None 인 경우
                    print('Evaluation error')
                    loop_escape = True #terminate the program
                    break
                else:
                    divide_popped = popped_6 / popped_5 #나눠서 push
                    if divide_popped.is_integer(): #int면 int형식으로 push
                        stack.push(mystack, int(divide_popped))
                    else: #나머지는 그대로 push
                        stack.push(mystack, divide_popped)


            elif k == '-':
                popped_7 = stack.pop(mystack)
                popped_8 = stack.pop(mystack)
                if popped_7 == None or popped_8 == None: #연산자 둘 중 하나가 None 인 경우
                    print('Evaluation error')
                    loop_escape = True #terminate the program
                    break
                else:
                    minus_popped = popped_8- popped_7
                    stack.push(mystack, minus_popped)
            else:
                stack.push(mystack, int(k))
