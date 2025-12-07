# Day 6 — Python Functions Projects

This folder contains projects for Day 6, focusing on **real Python functions**:

## Concepts Practiced

- Function definitions with `def`
- Parameters and return values
- Scope (`global` vs local variables)
- Helper functions
- Basic functional programming patterns
- Error handling

## Projects

### 1. Temperature Converter
- Converts between Celsius and Fahrenheit.
- Uses three separate functions:
  - `to_celsius(f: float) -> float`
  - `to_fahrenheit(c: float) -> float`
  - `convert()` — handles user input/output
- Demonstrates proper function separation, input validation, and scope.

### 2. Bank Account Simulator
- Simulates a simple bank account system.
- Functions:
  - `deposit(amount: float) -> float`
  - `withdraw(amount: float) -> float | None`
  - `show_balance() -> None`
  - `bank_menu()` — interactive menu
- Focus on **state management** and correct use of `global`.

### 3. Text Analyzer
- Analyzes a paragraph of text for:
  - Total words
  - Unique words
  - Most common word(s)
  - Number of sentences
- Uses helper functions:
  - `clean_text(text: str) -> str`
  - `split_into_sentences(text: str) -> list`
  - `analyze_text(text: str) -> dict`
- Demonstrates **modular design** and dictionary usage.