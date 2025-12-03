# PROJECT 1 — Grade Calculator
import sys

scores = []

for _ in range(3):
    score = float(input('Enter your score: '))
    if not 0 <= score <= 100: 
        print('Score must be between 0 and 100.')
        sys.exit()
    scores.append(score)

average = round(sum(scores)/len(scores), 1)

if average >= 90: grade = 'A'
elif average >= 80: grade = 'B'
elif average >= 70: grade = 'C'
elif average >= 60: grade = 'D'
else: grade = 'F'

print(f'Your average score is {average} and your grade is {grade}')
