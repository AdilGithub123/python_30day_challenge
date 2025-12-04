""" PROJECT 1 — Sum of Even Numbers

Requirements:
1. Ask user for 5 numbers
2. Store them in a list
3. Calculate and print:
    3.1 total sum
    3.2 sum of even numbers only

Focus:
Loops + list building.
"""

numbers = [float(input('Enter the number: ')) for _ in range(5)]
total = 0
even_sum = 0

for num in numbers:
    total += num
    if num % 2 == 0:
        even_sum += num

print(f'The total is {total} and the sum of even numbers is {even_sum}')