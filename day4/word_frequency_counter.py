"""
PROJECT 3 — Word Frequency Counter

This is your first tiny data-processing tool.

Requirements:
1. Ask user for a sentence
2. Normalize everything to lowercase
3. Remove punctuation (.,!?)
4. Split into words
5. Count occurrences of each word
6. Print something like:
apple: 2
banana: 1
orange: 3

Hints:
1. Use .lower()
2. Use .replace()
3. Use split()
4. Use a dictionary for counting:
counts = {}
for word in words:
    counts[word] = counts.get(word, 0) + 1
"""

sentence = input('Enter a sentence: ').lower()

for p in '.,!?':
    sentence = sentence.replace(p, '')

words = sentence.split()

counts = {}
for word in words:
    counts[word] = counts.get(word, 0) + 1

for word, count in counts.items():
    print(f'{word}: {count}')