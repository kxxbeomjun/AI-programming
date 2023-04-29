#lab4_p5.py
#lab2_p4 코드 차용

# program greeting:
print('This program will convert temperatures (Fahrenheit/Celsius)')
print('Enter (F) to convert Fahrenheit to Celsius')
print('Enter (C) to convert Celsius to Fahrenheit')
selection = input("Enter selection: ")

if selection == 'C':
      # get temperature in Celsius:
      celsius = int(input('Enter temperature to convert: '))
      while celsius < -273.15: #잘못된 입력 계속받는 것
            celsius = int(input('Enter temperature to convert: '))
      # convert C to F
      fahren = (celsius * 9/5) + 32
      # print result:
      print(celsius, 'degrees Celsius equals',
            format(fahren, '.1f'), 'degrees Fahrenheit')
elif selection =='F':
      # get temperature in Fahrenheit:
      fahren = int(input('Enter temperature to convert: '))
      while fahren < -459.67: #잘못된 입력 계속받는 것
            fahren = int(input('Enter temperature to convert: '))

      # convert Fahrenheit to Celsius:
      celsius = (fahren - 32) * 5 / 9

      # print result:
      print(fahren, 'degrees Fahrenheit equals',
            format(celsius, '.1f'), 'degrees Celsius')
