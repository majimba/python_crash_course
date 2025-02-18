# Program: Famous Quotes
# Author: Chawana Maseka
# Date: February 18, 2025
# Description: Displays a famous quote with proper string formatting

# Working with Quotes and String Formatting
# This example demonstrates:
# 1. Storing strings in variables
# 2. Using f-strings for complex string formatting
# 3. Handling quotes within strings using escape characters

# Store the person's name in a variable for easy reuse
famous_person = "Aristotle"

# Store the quote in a separate variable
# Using a separate variable makes the code more readable and maintainable
quote = "It is a shame for a man to grow old without seeing the beauty and strength of which his body is capable"

# Combine the person and quote using an f-string
# Note the use of escaped quotes (\") to properly format the quotation
# The .\" at the end adds a period inside the quotes
print(f"{famous_person} once said, \"{quote}.\"")

# Alternative ways to format this (commented out):
# 1. Using concatenation:
# print(famous_person + ' once said, "' + quote + '."')
# 
# 2. Using .format() method:
# print('{} once said, "{}"'.format(famous_person, quote))