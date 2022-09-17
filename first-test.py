number1 = float(input('number 1: '))
number2 = float(input('Number 2: '))
x = input('x: ')

calc = 0

if x == '+':
    calc = number1 + number2
elif x == '-':
    calc = number1 - number2
elif x == '*':
    calc = number1 * number2
elif x == '/':
    calc = number1 / number2
else:
    print('Error!')

print(f'Answer: {calc} ')
