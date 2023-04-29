# program greeting:
print('This program will convert degrees Celsius to degrees Fahrenheit')

# get temperature in Celsius:
celsius = float(input('Enter degrees Celsius: '))

# convert C to F
fahren = (celsius * 9/5) + 32

# print result:
print(celsius, 'degrees Celsius equals',
      format(fahren, '.1f'), 'degrees Fahrenheit')
