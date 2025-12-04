""" PROJECT 2 — Shopping List Manager

Requirements:
1. Start with an empty list
2. Let user repeatedly:
    A. add items
    B. remove items
    C. view items
    D. exit

But you must use a while loop.

Focus:
while loops, lists, branching.
"""

shopping_list = []

while True:
    user_choice = input('''Pick one of them:
A. Add item
B. Remove item
C. View list
D. Exit
''').lower()
    if user_choice not in ('a', 'b', 'c', 'd'):
        print('Input not valid.')
        continue
    elif user_choice == 'a':
        item = input('Enter the item: ')
        shopping_list.append(item)
    elif user_choice == 'b':
        item = input('Enter the item: ')
        if item in shopping_list:
            shopping_list.remove(item)
        else:
            print('Item not found.')
    elif user_choice == 'c':
        if shopping_list:
            for idx, item in enumerate(shopping_list, start=1):
                print(f'{idx}. {item}')
        else:
            print('List is empty.')
    else:
        break