# Day 7 — Errors & Exception Handling

Today’s focus: building code that **refuses to crash** even when users behave like gremlins.

## Concepts Covered
- `try / except` blocks  
- Handling specific exceptions (`ValueError`, ZeroDivisionError patterns)  
- Input validation  
- Designing resilient CLI interfaces  
- Defensive programming mindset  
- Preventing user-caused crashes  
- Clean program flow + graceful exits

---

## Project — Resilient CLI Calculator

A menu-driven command-line calculator that:
- Accepts: Add, Subtract, Multiply, Divide, Exit  
- Rejects invalid menu choices  
- Rejects non-numeric input (with clean recovery)  
- Prevents division by zero  
- Runs inside a continuous loop until user exits  
- Never crashes due to user errors

### Behaviors:
- Menu loops forever until the user chooses Exit  
- Each operation validates both operands  
- Division checks `num2 == 0` before attempting  
- Errors are handled with clear messages, not crashes  
- All results are displayed cleanly

This is the first project that forces defensive thinking — not just “make it work,” but “make it unbreakable.”

---

## Files Added
- `day07/README.md`
- `day07/cli_calculator.py`

---
