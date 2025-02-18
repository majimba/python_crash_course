# Program: Apostrophe Usage
# Author: Chawana Maseka
# Date: February 18, 2025
# Description: Demonstrates proper use of apostrophes in string literals

# Using quotes in strings
# When a string contains an apostrophe, use double quotes to enclose the string
# This avoids syntax errors that would occur with single quotes

message = "One of Python's strengths is its diverse community"  # Works fine with double quotes
print(message)

# The following would cause an error because Python can't identify where the string ends:
# message = 'One of Python's strengths is its diverse community'  # SyntaxError

# If you need to use double quotes in your string, you can enclose it in single quotes:
# message = 'The instructor said "Python is fun!"'