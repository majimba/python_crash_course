# Program: Chapter 1 Notes
# Author: Chawana Maseka
# Date: February 18, 2025
# Description: Contains notes and examples from Chapter 1 of Python Crash Course

# Chapter 1: Getting Started with Python
# This file demonstrates basic Python concepts and syntax

# In Python, we can print text to the screen using the print() function
# The text inside quotes is called a string - it's a sequence of characters
print("Hello World!")

# Comments like these help explain code and are ignored by Python
# Single-line comments start with a #
"""
Multi-line comments use three quotes
They can span multiple lines
Python will ignore all text between the triple quotes
"""

# Variables: Store data that can be used later in the program
message = "Hello Python world!"
print(message)  # Using a variable in a print statement

# Variables can be changed - they are "variable" after all
message = "Hello Python Crash Course world!"
print(message)  # The new value is printed

# Python's naming rules for variables:
# 1. Can only contain letters, numbers, and underscores
# 2. Can't start with a number
# 3. No spaces allowed - use underscores
# 4. Can't use Python keywords
# 5. Should be short but descriptive

# Good variable names
first_name = "ada"
last_name = "lovelace"
full_name = first_name + " " + last_name  # String concatenation
print(full_name)

# String Methods - Python has many built-in methods to modify strings
print(full_name.title())  # Capitalizes first letter of each word
print(full_name.upper())  # Converts to uppercase
print(full_name.lower())  # Converts to lowercase

# Common Errors to Watch For:
# 1. Syntax Errors: When Python doesn't understand your code
# 2. NameErrors: Using a variable before defining it
# 3. TypeError: Mixing different types of data incorrectly

# Examples of potential errors (commented out to prevent crashes):
# print(undefined_variable)    # NameError
# print('5' + 5)              # TypeError
# print("Unclosed string      # SyntaxError

# The Zen of Python - Python's guiding principles
# You can view these by typing 'import this' in a Python shell
# Key principles include:
# - Simple is better than complex
# - Readability counts
# - Explicit is better than implicit