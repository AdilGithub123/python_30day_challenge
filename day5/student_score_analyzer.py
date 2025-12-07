"""
PROJECT 1 — Student Score Analyzer

Use lists + dicts properly.

Requirements:
1. Ask user for number of students
2. For each student:
    - name
    - score
3. Store them in a dictionary like: {"Alice": 90, "Bob": 72, ...}
4. Print:
    - highest scoring student
    - lowest scoring student
    - average score
    - list of students above the average
"""
number_of_students = int(input('Number of students: '))

student_scores = {}

for _ in range(number_of_students):
    name = input('Student name: ')
    score = float(input('Student score: '))
    student_scores[name] = score

scores = list(student_scores.values())
average = sum(scores) / len(scores)

highest_score = max(scores)
lowest_score = min(scores)

highest_students = [name for name, score in student_scores.items() if score == highest_score]
lowest_students = [name for name, score in student_scores.items() if score == lowest_score]
above_average_students = [name for name, score in student_scores.items() if score > average]

print(f'Highest scoring student(s): {highest_students}')
print(f'Lowest scoring student(s): {lowest_students}')
print(f'Average score: {average}')
print(f'Students above average: {above_average_students}')