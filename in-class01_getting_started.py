# =============================================================
# Week 1 — Getting Started with Python
# IT-1051: Introduction to Programming | In-Class Code
# =============================================================


# -------------------------------------------------------------
# 1. What is Programming?
# -------------------------------------------------------------
# A program is a set of instructions that tells a computer what to do.
# Python is a high-level, interpreted language, so it's easy to read and write.
# We write code in VS Code, and Python runs it line by line, top to bottom.

# My first Python program
print("Hello, World!")
print("My name is James")
print("Welcome to IT-1051")


# -------------------------------------------------------------
# 2. Variables and Assignments
# -------------------------------------------------------------
# A variable is a named container that holds a value.
# The = sign assigns the value on the right to the name on the left.
# Rules and conventions for variable names:
#   - They are case sensitive: name and Name are different variables
#   - Use snake_case (my_variable, not myVariable)
#   - They can't start with a number
#   - They can't be reserved words like if, for, while

name = "Maya"       # text
age = 25            # whole number
gpa = 3.8           # decimal number
is_student = True   # True/False value

# Print the value stored in each variable
print(name)
print(age)
print(gpa)
print(is_student)


# -------------------------------------------------------------
# 3. Data Types
# -------------------------------------------------------------
# int   - whole numbers: 42, -7, 0
# float - decimal numbers: 3.14, -2.5
# str   - text: "Hello", "Python"
# bool  - True or False

my_int = 42
my_float = 3.14
my_str = "Hello Python"
my_bool = True

# type() tells us what kind of data a variable holds
print(type(my_int))     # <class 'int'>
print(type(my_float))   # <class 'float'>
print(type(my_str))     # <class 'str'>
print(type(my_bool))    # <class 'bool'>


# -------------------------------------------------------------
# 4. Input and Output
# -------------------------------------------------------------
# print() displays output to the screen.
# input() reads what the user types. It ALWAYS returns a string.

# Basic output
print("Hello!")
print("Hello", "World")     # multiple values are separated by a space
print("Hello", end=" ")     # end=" " keeps the next print on the same line
print("World")

# User input
name = input("Enter your name: ")
print("Hello,", name)

# Input with type conversion: wrap input() in int() to get a number
age = int(input("Enter your age: "))
print("You are", age, "years old")

# Try it together: ask for name and favorite number
name = input("What is your name? ")
number = int(input("What is your favorite number? "))
print("Hello", name + "! Your favorite number is", number)


# -------------------------------------------------------------
# 5. Arithmetic Operators
# -------------------------------------------------------------
# +   addition
# -   subtraction
# *   multiplication
# /   division (always returns a float)
# //  floor division (drops the decimal part)
# %   modulus (the remainder)
# **  exponent

num1 = 16
num2 = 3

print(num1 + num2)    # 19
print(num1 - num2)    # 13
print(num1 * num2)    # 48
print(num1 / num2)    # 5.333...
print(num1 // num2)   # 5
print(num1 % num2)    # 1
print(num1 ** num2)   # 4096

# Real-world example: calculate total cost
price = 9.99
quantity = 3
total = price * quantity
print("Total:", total)


# -------------------------------------------------------------
# 6. f-strings
# -------------------------------------------------------------
# f-strings let us embed variables directly in a string.
# Put f before the opening quote, and variable names inside { }.

name = "Maya"
age = 25
gpa = 3.8

# Old way: joining strings with +, and converting numbers with str()
print("My name is " + name + " and I am " + str(age) + " years old.")

# f-string way: cleaner and easier to read
print(f"My name is {name} and I am {age} years old.")
print(f"My GPA is {gpa:.2f}")   # :.2f formats to two decimal places


# -------------------------------------------------------------
# 7. Errors
# -------------------------------------------------------------
# Syntax error  - the code is not valid Python (typo, missing colon, etc.)
# Runtime error - the code starts running but crashes (divide by zero, wrong type)
# Logic error   - the code runs but produces the wrong result

# Syntax error: missing closing parenthesis.
# This line is commented out because it would stop the whole file from running.
# Uncomment it to see the error.
# print("Hello"

# Runtime error: crashes if the user enters 0
num = int(input("Enter a number: "))
result = 10 / num

# Logic error: no crash, but the answer is wrong
total = 10 + 5
average = total / 3    # should be / 2 (there are only two numbers)
print(f"Average: {average}")


# -------------------------------------------------------------
# 8. Math Module
# -------------------------------------------------------------
# Python has a built-in math module with useful functions.
# Use import math to access it (imports usually go at the top of a file).

import math

print(math.sqrt(16))    # 4.0      square root
print(math.pi)          # 3.14159... the constant pi
print(math.ceil(4.3))   # 5        round up
print(math.floor(4.7))  # 4        round down
print(math.fabs(-7))    # 7.0      absolute value (as a float)


# -------------------------------------------------------------
# In-Class Exercise
# -------------------------------------------------------------
# Write a program that:
#   - Asks the user for their name
#   - Asks for two numbers
#   - Calculates and prints the sum, difference, product, and quotient
#   - Uses f-strings to format the output neatly

# Solution:
name = input("Enter your name: ")
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print(f"\nHello {name}! Here are your results:")   # \n adds a blank line
print(f"Sum: {num1 + num2}")
print(f"Difference: {num1 - num2}")
print(f"Product: {num1 * num2}")
print(f"Quotient: {num1 / num2:.2f}")
