""" 
PROJECT 2 — Email Validator

Goal: Very basic validation (NOT real RFC rules, don't worry).

Requirements:
Input: a string (email)
Valid if ALL are true:
    1. Contains exactly one "@"
    2. Has at least one "." after the "@"
    3. No spaces
    4. Username (before @) is not empty
    5. Domain (after @) is not empty

Output:
    1. "Valid email"
    2. "Invalid email"
"""

email = input('Please enter your email: ').strip()

if email.count('@') != 1:
    print('Invalid email')
else:
    user, domain = email.split('@')
    if not user:
        print('Invalid email')
    elif not domain or '.' not in domain:
        print('Invalid email')
    elif ' ' in email:
        print('Invalid email')
    else:
        print('Valid email')