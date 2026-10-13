# =============================================================
# Week 4 — Strings (cont'd)
# IT-1051: Introduction to Programming | In-Class Code
# =============================================================


# -------------------------------------------------------------
# 1. Review Week 3
# -------------------------------------------------------------
# Quick review questions:
#   - How do you get the length of a string?
#   - What does text[0:5] return?
#   - How do you reverse a string using slicing?
#   - How do you convert a string to an integer?


# -------------------------------------------------------------
# 2. Advanced String Formatting
# -------------------------------------------------------------
# Field width controls how many characters wide the output is.
# Alignment:  <  left     >  right     ^  center
# Floating point precision: .1f = one decimal place, .2f = two, etc.
# Together these are useful for creating formatted tables.

name = "Alice"
score = 95.5

# Field width: name is left-aligned in 10 characters,
# score is right-aligned in 6 characters with 1 decimal place
print(f"{name:<10} {score:>6.1f}")
print(f"{'Bob':<10} {87.3:>6.1f}")
print(f"{'Charlie':<10} {92.0:>6.1f}")

# Center align in 30 characters
print(f"{'REPORT':^30}")

# "-" * 30 repeats the dash 30 times to make a divider line
print(f"{'-' * 30}")


# -------------------------------------------------------------
# 3. String Methods
# -------------------------------------------------------------
# A method is a function that belongs to a value.
# Call it with a dot: text.upper()
#   upper()   converts to uppercase
#   lower()   converts to lowercase
#   strip()   removes whitespace from the beginning and end
#   replace() replaces one substring with another
#   find()    returns the index where a substring starts (-1 if not found)
# Methods return a NEW string. The original is unchanged (strings are immutable).

text = "  Hello, Python!  "    # note the spaces at both ends

# (The quotes in the comments below just show where the spaces are.
#  Python doesn't print the quotes.)
print(text.upper())                       # "  HELLO, PYTHON!  "
print(text.lower())                       # "  hello, python!  "
print(text.strip())                       # "Hello, Python!"
print(text.strip().upper())               # "HELLO, PYTHON!"  (methods can be chained)
print(text.replace("Python", "World"))    # "  Hello, World!  "
print(text.find("Python"))                # 9
print(text.find("Java"))                  # -1 (not found)


# -------------------------------------------------------------
# 4. Splitting and Joining Strings
# -------------------------------------------------------------
# split() breaks a string into a list of smaller strings.
#   With no argument, it splits on whitespace (spaces, tabs, newlines).
#   With an argument, it splits on that character: split(",")
# join() does the opposite: combines a list of strings into one string.
#   The string before .join is placed between each item.

# split() on whitespace
sentence = "Python is a great language"
words = sentence.split()
print(words)    # ['Python', 'is', 'a', 'great', 'language']

# split() on commas, like a line from a CSV file
csv_line = "Alice,25,Cleveland"
parts = csv_line.split(",")
print(parts)    # ['Alice', '25', 'Cleveland']

# join() with a space between items
words = ["Python", "is", "awesome"]
result = " ".join(words)
print(result)    # Python is awesome

# join() with a dash between items
result2 = "-".join(["2026", "01", "15"])
print(result2)    # 2026-01-15


# -------------------------------------------------------------
# 5. Introduction to AI-Assisted Programming
# -------------------------------------------------------------
# GitHub Copilot is an AI coding assistant built into VS Code.
# It suggests code as you type, based on your comments and the
# code around it.
# AI tools are powerful but not always correct. You must evaluate the output.
# Good prompting (clear, specific comments) produces better suggestions.
#
# Key questions to ask about AI-generated code:
#   - Does it actually solve the problem?
#   - Does it handle edge cases (empty string, single name)?
#   - Is it readable and well-organized?
#   - Do I understand what every line does?

# Demo: ask Copilot to complete this function.
# Write a function that takes a full name and returns the initials
def get_initials(full_name):
    # Copilot's suggestion appears here
    pass    # pass is a placeholder that does nothing, so the file still runs


# -------------------------------------------------------------
# 6. In-Class Exercise
# -------------------------------------------------------------
# Write a program that asks the user for a sentence, then prints:
#   - the sentence in uppercase
#   - the sentence with all vowels replaced with *
#   - the number of words
#   - each word on its own line

# Solution:
sentence = input("Enter a sentence: ")

# Uppercase
print(sentence.upper())

# Replace vowels: loop through each vowel and replace it with *
no_vowels = sentence
for vowel in "aeiouAEIOU":
    no_vowels = no_vowels.replace(vowel, "*")
print(no_vowels)

# Word count: split into a list of words, then count the items
words = sentence.split()
print(f"Words: {len(words)}")

# Each word on its own line
for word in words:
    print(word)
