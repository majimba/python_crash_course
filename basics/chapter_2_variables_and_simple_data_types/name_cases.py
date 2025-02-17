# String Case Methods Exercise
# This program demonstrates the three main case methods in Python:
# - lower(): converts string to all lowercase
# - upper(): converts string to all uppercase
# - title(): capitalizes the first letter of each word

# Store the name in a variable
name = "Majimba"

# 1. lowercase method
# Converts all characters to lowercase
# Useful for case-insensitive comparisons
print(f"{name.lower()}")  # Output: majimba

# 2. uppercase method
# Converts all characters to uppercase
# Often used for emphasis or displaying constants
print(f"{name.upper()}")  # Output: MAJIMBA

# 3. title case method
# Capitalizes the first letter of each word
# Commonly used for formatting names and titles
print(f"{name.title()}")  # Output: Majimba

# Note: These methods don't modify the original string
# They return a new string with the changes applied
# The original 'name' variable remains unchanged

# Common use cases:
# - lower(): user input validation
# - upper(): displaying headings or warnings
# - title(): formatting proper nouns (names, places)