""" PROJECT 3 — Number Guessing Game

Requirements:
1. Program secretly chooses a number between 1-20
2. User keeps guessing until correct
3. Give hints:
    3.1 “Too high”
    3.2 “Too low”
4. Count attempts
5. Stop with break when guessed right

Focus:
loops + conditionals + logic.
"""

import random

random_number = random.randint(1, 20)
attempts = 0

while True:
    attempts += 1

    try:
        guessed_number = int(input('Guess a number between 1 and 20: '))
    except ValueError:
        print('Enter a valid number.')
        continue
    
    if guessed_number > random_number:
        print('Too high')
    elif guessed_number < random_number:
        print('Too low')
    else:
        print(f'Congratulations! You solved it in {attempts} attempts!')
        break