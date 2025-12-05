""" 
PROJECT 1 — Name Normalizer 

Goal: Clean up a user's messy name input.

Requirements:
1. Ask the user for a name (string)
2. Remove extra spaces
3. Capitalize the first letter of each word
4. Print the cleaned name

Concepts used:
.strip()
.split()
.title()
" ".join()
"""

name = input('Please enter your name: ').strip()
cleaned = ' '.join(name.split()).title()
print(cleaned)