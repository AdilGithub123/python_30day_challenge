# PROJECT 1 — Age Group Classifier

import sys

age = int(input('Enter your age: '))

if not 0 <= age <= 120: 
    print('Invalid age.')
    sys.exit()
elif age >= 65:
    group = 'Senior'
elif age >= 20:
    group = 'Adult'
elif age >= 13:
    group = 'Teen'
else:
    group = 'Child'

print(f'Your age group is {group}')