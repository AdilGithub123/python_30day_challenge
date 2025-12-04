# PROJECT 3 — Simple Calculator (With Error Handling)

import sys

num1 = float(input('Enter the first number: '))
operator = input('Enter the operator (+, -, * or /): ')
num2 = float(input('Enter the second number: '))

if operator not in ('+', '-', '*', '/'):
    print('Invalid operator.')
    sys.exit()
elif operator == '/' and num2 == 0:
    print('Cannot divide by zero.')
    sys.exit()
elif operator == '+':
    result = num1 + num2
elif operator == '-':
    result = num1 - num2
elif operator == '*':
    result = num1 * num2
elif operator == '/':
    result = num1 / num2

print(f'{num1} {operator} {num2} = {result}')