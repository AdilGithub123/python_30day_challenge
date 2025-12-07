"""
PROJECT 2 — Unique Word Extractor

This trains sets.

Requirements:
1. Ask user for a paragraph
2. Normalize to lowercase
3. Remove punctuation
4. Split into words
5. Store the unique words in a set
6. Print:
    - number of unique words
    - the unique words in alphabetical order
"""
paragraph = input('Enter a paragraph: ').lower()

for c in '.,!?':
    paragraph = paragraph.replace(c, '')

words = paragraph.split()
unique_words = set(words)

print(f'Number of unique words: {len(unique_words)}')
print(f'Unique words (alphabetical): {sorted(unique_words)}')