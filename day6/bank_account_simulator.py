"""
PROJECT 2 — Bank Account Simulator (Functions + State + Logic)

You're building a tiny, proper system using functions.

The account starts with: balance = 0

You must write these functions:
1. deposit(amount) → increases balance, returns new balance
2. withdraw(amount) →
    - if amount > balance → return None
    - else subtract and return new balance
3. show_balance() → prints current balance
4. bank_menu() →
    - loop until user chooses exit
    - let the user:
        - deposit
        - withdraw
        - view balance
        - exit
- use the above functions
- handle invalid inputs

Rules:
1. You MUST use return values correctly.
2. You MUST keep balance in a controlled scope.
"""
balance = 0

def deposit(amount: float) -> float:
    global balance
    balance += amount
    return balance

def withdraw(amount: float):
    global balance
    if amount > balance:
        return None
    balance -= amount
    return balance

def show_balance():
    print(f'Current balance: {balance}')

def bank_menu():
    while True:
        choice = input('Menu: Deposit, Withdraw, View Balance, Exit\n').lower()
        if choice.startswith('d'):
            try:
                amount = float(input('Enter the amount to deposit: '))
                print(f'New balance: {deposit(amount)}')
            except ValueError:
                print('Enter a numeric value!')
        elif choice.startswith('w'):
            try:
                amount = float(input('Enter the amount to withdraw: '))
                result = withdraw(amount)
                if result is None:
                    print('Insufficient funds!')
                else:
                    print(f'New balance: {result}')
            except ValueError:
                print('Enter a numeric value!')
        elif choice.startswith('v') or choice.startswith('b'):
            show_balance()
        elif choice.startswith('e'):
            break
        else:
            print('Invalid choice, try again!')

bank_menu()