# PROJECT 3 — Unit Converter (KM ↔ Miles)
import sys

user_choice = input('Choose A or B\nA. km -> miles\nB. miles -> km\n').lower()

if user_choice not in ('a', 'b'): 
    print('Value invalid!')
    sys.exit()

value = float(input('Enter the value: '))

if user_choice == 'a': converted = round(value * 0.621371, 2)
else: converted = round(value / 0.621371, 2)

print(f'The converted value is {converted}')
