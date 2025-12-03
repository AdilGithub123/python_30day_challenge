# PROJECT 2 — Simple Interest Calculator

principal = float(input('Enter the principal: '))
rate = float(input('Enter the rate (in %): '))
time = float(input('Enter the time (in years): '))

interest = principal * rate * time / 100
total = principal + interest
print(f'The total amount is {round(total, 2)} and the interest is {round(interest, 2)}')
