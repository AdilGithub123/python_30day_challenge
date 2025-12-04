# PROJECT 2 — Password Strength Checker

password = input('Enter a password: ')

has_digit = any(c.isdigit() for c in password)
has_alpha = any(c.isalpha() for c in password)

if len(password) >= 8 and has_digit and has_alpha:
    print('Password is strong.')
else:
    print('Password is weak.')