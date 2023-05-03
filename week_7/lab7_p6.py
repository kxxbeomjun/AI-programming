#lab7_p6.py

#stack.py를 import
import stack

#새로운 stack 만들기
mystack = stack.getStack()
check_nested = True #return default값

symbol = list(input('Enter parentheses and/or braces: '))


for k in range(len(symbol)):
    if symbol[k] == '(' or symbol[k] == '{' : #왼쪽괄호는 push
        stack.push(mystack, symbol[k])
    elif symbol[k] == ')': #오른쪽괄호는 pop해서 짝맞는지 확인 '()' 짝확인
        popped_symbol = stack.pop(mystack)
        if popped_symbol == '(':
            pass
        else:
            check_nested = False
            break
    else: #오른쪽괄호는 pop해서 짝맞는지 확인 '{}' 짝확인
        popped_symbol2 = stack.pop(mystack)
        if popped_symbol2 == '{':
            pass
        else:
            check_nested = False
            break

#stack에 남아있는거 있으면 제대로 정렬되지 않은것
if stack.isEmpty(mystack):
    pass
else:
    check_nested = False

#print 구문
if check_nested:
    print('Nested properly.')
else:
    print('Not properly nested.')

