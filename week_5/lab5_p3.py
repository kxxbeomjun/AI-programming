#lab5_p3.py

#boolean flag
loop_flag = False
list = []

while not loop_flag:
    int_input = int(input('Enter an integer: '))
    if int_input == 0:
        loop_flag = True #0 입력하면 loop escape
    else:
        if int_input > 100: #제한조건
            list.append('over')
        elif int_input < -100: #제한조건
            list.append('under')
        else: 
            list.append(int_input)

#print
print(list)
