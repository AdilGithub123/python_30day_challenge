menu = """--- Simple CLI Calculator ---
Add (A)
Subtract (S)
Multiply (M)
Divide (D)
Exit (E)
Choose an option:\n"""

while True:
    choice = input(menu).lower()

    if choice not in ('a', 's', 'm', 'd', 'e'):
        print('Invalid choice, please try again.')
        continue

    if choice == 'e':
            print('Goodbye!')
            break
    
    # get numbers
    try:
        num1 = int(input('Enter first number: '))
        num2 = int(input('Enter second number: '))
    except ValueError:
        print('Your input should be numeric, try again.')
        continue

    # division safety
    if choice == 'd' and num2 == 0:
        print('Cannot divide by zero.')
        continue

    # perform operation
    if choice == 'a':
        result = num1 + num2
    elif choice == 's':
        result = num1 - num2
    elif choice == 'm':
        result = num1 * num2
    else:  # choice == 'd'
        result = num1 / num2
    
    print(f'Result: {result}')
