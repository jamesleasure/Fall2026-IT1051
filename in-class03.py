# =============================================================
# Week 3 — Text and Strings
# IT-1051: Introduction to Programming | In-Class Code
# =============================================================


# -------------------------------------------------------------
# 1. Review Week 2
# -------------------------------------------------------------
# Quick review questions:
#   - What does // do?
#   - What does % return?
#   - How do you import a module?
#   - Name two escape sequences


# -------------------------------------------------------------
# 2. String Basics
# -------------------------------------------------------------
# A string is a sequence of characters.
# Strings are immutable: you cannot change individual characters.
# Use single or double quotes to create a string.
# Use len() to get the length (number of characters, spaces included).

message = "Hello, Python!"

print(len(message))    # 14
print(message[0])      # H
print(message[-1])     # !
print(message[0:5])    # Hello
print(message[7:])     # Python!
print(message[:5])     # Hello


# -------------------------------------------------------------
# 3. String Indexing
# -------------------------------------------------------------
# Characters are accessed by index, starting at 0.
# Negative indexes count backward from the end.
#   word[0]  is the first character
#   word[-1] is the last character
#
#    P   y   t   h   o   n
#    0   1   2   3   4   5
#   -6  -5  -4  -3  -2  -1

word = "Python"

print(word[0])     # P
print(word[1])     # y
print(word[-1])    # n
print(word[-2])    # o

# Using an index that doesn't exist causes an IndexError.
# This line is commented out because it would crash the program.
# print(word[10])


# -------------------------------------------------------------
# 4. String Slicing
# -------------------------------------------------------------
# Slicing extracts a portion of a string.
# Syntax: string[start:end:step]
#   - start is inclusive (included)
#   - end is exclusive (stops just before it)
#   - leaving out start means "from the beginning"
#   - leaving out end means "to the end of the string"
#   - step is how many characters to move each time (default 1)

text = "Hello, World!"

print(text[0:5])     # Hello
print(text[7:12])    # World
print(text[::2])     # Hlo ol!        (every 2nd character)
print(text[::-1])    # !dlroW ,olleH  (a step of -1 reverses the string)


# -------------------------------------------------------------
# 5. Type Conversions
# -------------------------------------------------------------
# int()   converts to an integer
# float() converts to a float
# str()   converts to a string
# input() always returns a string, so convert it before doing math.

# String to int
age_str = "25"
age_int = int(age_str)
print(age_int + 5)    # 30

# String to float
price = "9.99"
price_float = float(price)
print(price_float * 2)    # 19.98

# Number to string (needed to join it with + to other text)
num = 42
num_str = str(num)
print("Number: " + num_str)    # Number: 42

# Common pattern: convert input right away
age = int(input("Enter your age: "))
print(f"Next year you will be {age + 1}")


# -------------------------------------------------------------
# 6. f-string Formatting
# -------------------------------------------------------------
# Format specifiers go after a colon inside the { }:
#   :.2f   two decimal places
#   :10    minimum width of 10 characters
#          (text lines up left by default, numbers line up right)
#   :<10   left align in 10 characters
#   :>10   right align in 10 characters
#   :d     format as a whole number (integer)

price = 9.99
name = "Python Book"
stock = 142

# Basic f-string
print(f"Price: {price}")

# Two decimal places
print(f"Price: {price:.2f}")

# Field width and alignment: builds a neat table.
# Note: the header text uses single quotes inside the double-quoted f-string.
print(f"{'Product':<20} {'Price':>8} {'Stock':>6}")
print(f"{name:<20} {price:>8.2f} {stock:>6}")


# -------------------------------------------------------------
# 7. In-Class Exercise
# -------------------------------------------------------------
# Write a program that asks for a first and last name, then prints:
#   - the full name
#   - the initials
#   - the name reversed
#   - the length of the full name

# Solution:
first = input("Enter first name: ")
last = input("Enter last name: ")

full_name = first + " " + last
initials = first[0] + "." + last[0] + "."    # first character of each name
reversed_name = full_name[::-1]              # step of -1 reverses it

print(f"Full name: {full_name}")
print(f"Initials: {initials}")
print(f"Reversed: {reversed_name}")
print(f"Length: {len(full_name)}")
