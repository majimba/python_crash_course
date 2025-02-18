# Program: Full Name Formatting
# Author: Chawana Maseka
# Date: February 18, 2025
# Description: Demonstrates string concatenation and f-string formatting

# Using f-strings (formatted string literals)
# f-strings were introduced in Python 3.6 and are the preferred way to format strings
# They allow you to insert variables directly into string literals

first_name = "ada"
last_name = "lovelace"
# The f before the quotes creates an f-string
# Variables in curly braces {} are replaced with their values
full_name = f"{first_name} {last_name}"
print(f"{full_name.title()}")  # Using title() method inside an f-string

# Creating a message using f-strings
# This makes the output more personal and readable
message = f"Hello, {full_name.title()}!"
print(message)