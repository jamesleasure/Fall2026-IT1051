# =============================================================
# Week 5 — Decision Making
# IT-1051: Introduction to Programming | In-Class Code
# =============================================================

# -------------------------------------------------------------
# 1. Review Week 4
# -------------------------------------------------------------
# Quick review questions:
#   - What is a loop? What are the two main types in Python?
#   - What does range(1, 6) produce?
#   - How do you stop a loop early? How do you skip an iteration?
#   - What is a sentinel value?

# -------------------------------------------------------------
# 2. if / elif / else Statements
# -------------------------------------------------------------
# A conditional statement lets a program choose a different
# path based on whether a condition is True or False.
#
#   if condition:
#       # runs when condition is True
#   elif other_condition:
#       # runs when the first was False and this is True
#   else:
#       # runs when ALL conditions above were False
#
# Only ONE branch runs — Python checks from top to bottom and
# stops at the first True condition.

age = int(input("Enter your age: "))

if age >= 65:
    print("Senior discount applies.")
elif age >= 18:
    print("Adult price.")
elif age >= 13:
    print("Teen price.")
else:
    print("Child price.")

# -------------------------------------------------------------
# 3. Comparison Operators
# -------------------------------------------------------------
# These operators compare two values and return True or False.
#
#   ==   equal to
#   !=   not equal to
#   <    less than
#   >    greater than
#   <=   less than or equal to
#   >=   greater than or equal to
#
# Common mistake: using = (assignment) instead of == (comparison)

x = 10
print(x == 10)   # True
print(x != 5)    # True
print(x < 20)    # True
print(x >= 10)   # True

# -------------------------------------------------------------
# 4. Logical Operators
# -------------------------------------------------------------
# Combine multiple conditions into one expression:
#
#   and   — True only if BOTH sides are True
#   or    — True if EITHER side is True
#   not   — flips True to False, and False to True

score = 82
paid = True

if score >= 70 and paid:
    print("Eligible to continue.")

temperature = 95
humidity = 80

if temperature > 90 or humidity > 85:
    print("Heat advisory in effect.")

raining = False
if not raining:
    print("No umbrella needed.")

# -------------------------------------------------------------
# 5. Detecting Ranges
# -------------------------------------------------------------
# To check if a value falls within a range, combine two
# comparisons with 'and'.  Python also supports chained
# comparisons, which read more naturally.

grade = 78

# Traditional style
if grade >= 70 and grade < 80:
    print("C")

# Chained comparison — Pythonic and easier to read
if 70 <= grade < 80:
    print("C (chained)")

# Detecting ranges WITH gaps requires multiple elif branches
score = 55
if score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
elif score >= 60:
    print("D")
else:
    print("F")

# -------------------------------------------------------------
# 6. Nested if Statements
# -------------------------------------------------------------
# An if statement can live inside another if statement.
# Use nested ifs when a second decision only matters if the
# first condition is already True.
# Keep nesting shallow (1–2 levels) — deep nesting gets hard to read.

member = True
cart_total = 75

if member:
    if cart_total >= 50:
        print("Free shipping!")
    else:
        print("Members save 10% on shipping.")
else:
    print("Standard shipping rates apply.")

# -------------------------------------------------------------
# 7. Introduction to Testing
# -------------------------------------------------------------
# Testing means running your program with specific inputs and
# checking that it produces the expected output.
#
# Good test cases cover:
#   - Typical inputs (the normal case)
#   - Boundary values (the edges: exactly 18, exactly 0)
#   - Edge cases (empty string, negative numbers, very large values)
#
# Example test plan for a grade calculator:
#   Input 95  → expected output: A
#   Input 85  → expected output: B
#   Input 75  → expected output: C
#   Input 65  → expected output: D
#   Input 55  → expected output: F
#   Input 90  → expected output: A  (boundary — exactly 90)
#   Input 80  → expected output: B  (boundary — exactly 80)

# -------------------------------------------------------------
# 8. In-Class Exercise
# -------------------------------------------------------------
# Write a movie ticket price calculator.
# Ask the user for their age and whether it is before 5 PM (y/n).
# Rules:
#   - Children under 12:        $8.00
#   - Seniors 65 and older:     $9.00
#   - Everyone else:            $12.00
#   - Matinee (before 5 PM):    $2.00 discount for all ages
# Print the final ticket price.

print("\n--- Movie Ticket Calculator ---")
age = int(input("Enter your age: "))
matinee = input("Is it before 5 PM? (y/n): ").strip().lower()

if age < 12:
    price = 8.00
elif age >= 65:
    price = 9.00
else:
    price = 12.00

if matinee == "y":
    price -= 2.00

print(f"Your ticket price: ${price:.2f}")
