# =============================================================
# Week 6 — Decision Making (cont'd)
# IT-1051: Introduction to Programming | In-Class Code
# =============================================================

# -------------------------------------------------------------
# 1. Review Week 5
# -------------------------------------------------------------
# Quick review questions:
#   - What is the difference between = and ==?
#   - What does 'and' require vs. what does 'or' require?
#   - How do you check if a number is between 10 and 20?
#   - What does a nested if statement look like?

# -------------------------------------------------------------
# 2. Comparing Different Data Types
# -------------------------------------------------------------
# Python can compare strings, numbers, and booleans, but you
# need to make sure you're comparing the same type.
# input() always returns a string — convert before comparing numbers.

user_input = input("Enter a number: ")

# This compares a string to an integer — always False!
if user_input == 5:
    print("Got 5 (this will never print)")

# Convert first — then compare correctly
number = int(user_input)
if number == 5:
    print("You entered 5!")

# String comparisons are case-sensitive
answer = input("Type yes or no: ").strip().lower()
if answer == "yes":
    print("You said yes.")

# -------------------------------------------------------------
# 3. Membership Operators: in / not in
# -------------------------------------------------------------
# 'in' checks whether a value exists inside a sequence
# (string, list, tuple, etc.)
# 'not in' checks that it does NOT exist.

vowels = "aeiou"
letter = "e"
if letter in vowels:
    print(f"{letter} is a vowel.")

day = input("Enter a day: ").strip().lower()
weekend = ["saturday", "sunday"]
if day in weekend:
    print("It's the weekend!")
else:
    print("It's a weekday.")

# Checking for a substring inside a string
phrase = "Hello, World!"
if "World" in phrase:
    print("Found 'World' in the phrase.")

# -------------------------------------------------------------
# 4. Order of Evaluation (Operator Precedence)
# -------------------------------------------------------------
# Python evaluates conditions in this order:
#   1. Parentheses  ()
#   2. not
#   3. and
#   4. or
#
# Use parentheses to make your intent clear — don't rely on
# memorizing precedence rules.

x = 5
y = 10
z = 15

# 'and' binds more tightly than 'or'
result = x < y or y > z and z == 15   # reads as: (x<y) or ((y>z) and (z==15))
print(result)   # True

# Parentheses make it explicit and readable
result = (x < y) or (y > z and z == 15)
print(result)   # True — same result, much clearer intent

# -------------------------------------------------------------
# 5. Common Errors in Conditional Expressions
# -------------------------------------------------------------

# ERROR 1: Assignment instead of comparison
# if x = 5:          <- SyntaxError — use == instead
# if x == 5:         <- Correct

# ERROR 2: Forgetting that 'and' requires BOTH to be True
score = 85
# This reads wrong: checks 70 against nothing, then score
# if 70 < score < 90:  <- Actually fine in Python (chained comparison)

# ERROR 3: Duplicate conditions that can never both be True
age = 20
if age >= 18:
    print("Adult")
if age >= 21:          # This works, but...
    print("Can drink")
# A better approach uses elif so ranges don't overlap ambiguously.

# ERROR 4: Indentation errors — body must be indented
temperature = 72
if temperature > 70:
    print("It's warm outside.")   # Must be indented
# print("check")                  # <- This is OUTSIDE the if block

# -------------------------------------------------------------
# 6. The Ternary (Conditional) Expression
# -------------------------------------------------------------
# A compact one-line if/else for simple assignments.
# Syntax:  value_if_true  if  condition  else  value_if_false
#
# Use it for simple assignments — avoid it when logic is complex.

age = 20
status = "adult" if age >= 18 else "minor"
print(status)

price = 100
discount = 0.1 if price > 50 else 0.0
final = price - (price * discount)
print(f"Final price: ${final:.2f}")

# -------------------------------------------------------------
# 7. match / case  (Python 3.10+)
# -------------------------------------------------------------
# When you're checking one variable against many specific values,
# match/case is cleaner than a long chain of elif statements.
# Think of it as Python's version of switch/case in other languages.

day_num = int(input("Enter day number (1–7): "))

match day_num:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case 4:
        print("Thursday")
    case 5:
        print("Friday")
    case 6 | 7:          # '|' means "or" inside a case
        print("Weekend")
    case _:              # default — matches anything else
        print("Invalid day number")

# -------------------------------------------------------------
# 8. In-Class Exercise
# -------------------------------------------------------------
# Write a program that asks the user for a month name (e.g. "March")
# and prints how many days are in that month.
# Use 'in' with a list for months that share the same day count.
# Treat February as always having 28 days.

month = input("Enter a month name: ").strip().lower()

months_31 = ["january", "march", "may", "july",
             "august", "october", "december"]
months_30 = ["april", "june", "september", "november"]

if month in months_31:
    print(f"{month.capitalize()} has 31 days.")
elif month in months_30:
    print(f"{month.capitalize()} has 30 days.")
elif month == "february":
    print("February has 28 days (or 29 in a leap year).")
else:
    print("That doesn't look like a valid month name.")
