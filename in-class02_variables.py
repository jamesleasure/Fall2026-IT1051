# =============================================================
# Week 2 — Variables, Expressions, and Modules
# IT-1051: Introduction to Programming | In-Class Code
# =============================================================


# -------------------------------------------------------------
# 1. Review Week 1
# -------------------------------------------------------------
# Quick review questions:
#   - What is the difference between int and float?
#   - What does input() always return?
#   - What is an f-string?
#   - What is the difference between / and //?


# -------------------------------------------------------------
# 2. Numeric Types in Depth
# -------------------------------------------------------------
# Integers are whole numbers with no decimal point.
# Floats always have a decimal point.
# Python automatically chooses the type based on the value.

x = 5         # int
y = 5.0       # float (the .0 makes it a float)
z = 5 / 2     # float (/ always returns a float)
w = 5 // 2    # int (floor division of two ints gives an int)

print(type(x))    # <class 'int'>
print(type(y))    # <class 'float'>
print(type(z))    # <class 'float'>
print(type(w))    # <class 'int'>


# -------------------------------------------------------------
# 3. Division and Modulo
# -------------------------------------------------------------
# /   always returns a float
# //  returns the integer part of the division (floor division)
# %   returns the remainder

print(10 / 3)     # 3.3333...
print(10 // 3)    # 3
print(10 % 3)     # 1

# Real-world use of modulo: checking even or odd.
# If a number divided by 2 has no remainder, it's even.
number = 17
if number % 2 == 0:
    print("Even")
else:
    print("Odd")

# Convert minutes to hours and minutes.
# // gives the whole hours, % gives the leftover minutes.
total_minutes = 137
hours = total_minutes // 60
minutes = total_minutes % 60
print(f"{total_minutes} minutes is {hours} hours and {minutes} minutes")


# -------------------------------------------------------------
# 4. Operator Precedence
# -------------------------------------------------------------
# Python follows the standard math order of operations:
#   1. **             first
#   2. *  /  //  %    next
#   3. +  -           last
# Use parentheses to control the order.

print(2 + 3 * 4)       # 14, not 20 (multiplication happens first)
print((2 + 3) * 4)     # 20 (parentheses happen first)
print(2 ** 3 + 1)      # 9
print(10 / 2 + 3)      # 8.0
print(10 / (2 + 3))    # 2.0


# -------------------------------------------------------------
# 5. Compound Operators
# -------------------------------------------------------------
# Shorthand for updating a variable.
# x += 1 is the same as x = x + 1

x = 10
x += 5     # x = 15
x -= 3     # x = 12
x *= 2     # x = 24
x //= 4    # x = 6
print(x)   # 6

# Common use: keeping a running total
total = 0
total += 10
total += 25
total += 15
print(f"Total: {total}")   # 50


# -------------------------------------------------------------
# 6. Module Basics
# -------------------------------------------------------------
# A module is a file containing Python functions and variables.
# Use import to access a module.
# Use module.function() to call a function from a module.

import math

# Constants
print(math.pi)    # 3.14159...
print(math.e)     # 2.71828...

# Functions
print(math.sqrt(25))       # 5.0    square root
print(math.ceil(4.1))      # 5      round up
print(math.floor(4.9))     # 4      round down
print(math.pow(2, 8))      # 256.0  2 to the 8th power
print(math.log(100, 10))   # 2.0    log base 10 of 100


# -------------------------------------------------------------
# 7. Random Module
# -------------------------------------------------------------
# The random module generates random numbers.
# Useful for games, simulations, and testing.
# (Your output will be different each time you run this.)

import random

# Random integer between 1 and 6, including both ends (like a dice roll)
dice = random.randint(1, 6)
print(f"You rolled: {dice}")

# Random float between 0 and 1
chance = random.random()
print(f"Random chance: {chance:.2f}")

# Random choice from a list
colors = ["red", "blue", "green", "yellow"]
pick = random.choice(colors)
print(f"Random color: {pick}")


# -------------------------------------------------------------
# 8. Representing Text
# -------------------------------------------------------------
# Strings can use single or double quotes.
# Escape sequences (starting with a backslash) let us include
# special characters in a string.

print("Hello\nWorld")            # \n  newline
print("Hello\tWorld")            # \t  tab
print("She said \"Hello!\"")     # \"  quotes inside a string
print("C:\\Users\\James")        # \\  a single backslash

# Raw strings: the r prefix tells Python to ignore escape sequences
print(r"C:\Users\James")         # prints exactly as written


# -------------------------------------------------------------
# 9. Style Guidelines (PEP 8)
# -------------------------------------------------------------
# PEP 8 is Python's official style guide:
#   - Use 4 spaces for indentation
#   - Use snake_case for variable names
#   - Keep lines under 79 characters
#   - Add spaces around operators
#   - Add blank lines between sections

# Bad style: cramped, and the names don't tell you anything
x=5
y=10
z=x+y
print(z)

# Good style: descriptive names, spaces around operators
first_number = 5
second_number = 10
total = first_number + second_number
print(total)


# -------------------------------------------------------------
# In-Class Exercise
# -------------------------------------------------------------
# Write a program that:
#   - Asks the user to enter a distance in miles
#   - Converts it to kilometers (1 mile = 1.60934 km)
#   - Asks the user to enter a time in minutes
#   - Converts it to hours and remaining minutes
#   - Calculates and prints the speed in km/h
#   - Uses f-strings with two decimal places for all output

# Solution:
miles = float(input("Enter distance in miles: "))
total_minutes = int(input("Enter time in minutes: "))

kilometers = miles * 1.60934

# Hours and leftover minutes, for displaying the time
hours = total_minutes // 60
minutes = total_minutes % 60

# Total time as a decimal number of hours, for calculating speed
time_in_hours = total_minutes / 60
speed = kilometers / time_in_hours

print(f"\nDistance: {kilometers:.2f} km")
print(f"Time: {hours} hours and {minutes} minutes")
print(f"Speed: {speed:.2f} km/h")
