"""
PROJECT 1 — Temperature Converter (Proper Functions Only)

You must write three separate functions:
1. to_celsius(f) → returns Celsius
2. to_fahrenheit(c) → returns Fahrenheit
3. convert() →
    - asks the user: convert to C or to F
    - asks for the temperature
    - calls the correct function
    - prints the result
Rules:
    - Do NOT print inside to_celsius or to_fahrenheit. Only inside convert().
    - Validate input: if user enters something invalid, print an error message and stop.
"""
def to_celsius(f: float) -> float:
    return round((f - 32) * 5 / 9, 2)

def to_fahrenheit(c: float) -> float:
    return round(c * 9 / 5 + 32, 2)

def convert():
    try:
        choice = input('Convert to Celsius or Fahrenheit? ').lower()
        
        if choice.startswith('c'):
            temp = float(input('Enter temperature in Fahrenheit: '))
            print(f'Temperature in Celsius: {to_celsius(temp)}°C')
        elif choice.startswith('f'):
            temp = float(input('Enter temperature in Celsius: '))
            print(f'Temperature in Fahrenheit: {to_fahrenheit(temp)}°F')
        else:
            print('Invalid choice!')
    except ValueError:
        print('Temperature must be numeric!')

convert()