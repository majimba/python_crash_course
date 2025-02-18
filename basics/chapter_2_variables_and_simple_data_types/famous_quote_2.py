# Program: Famous Quotes 2
# Author: Chawana Maseka
# Date: February 18, 2025
# Description: Displays a famous quote using variables for author and quote

# Working with Quotes and String Formatting
# This example demonstrates:
# 1. Storing strings in variables
# 2. Using f-strings for complex string formatting
# 3. Creating a composite message from multiple variables

# Store the person's name in a variable
famous_person = "Aristotle"

# Store the quote in a separate variable
quote = "It is a shame for a man to grow old without seeing the beauty and strength of which his body is capable"

# Create a formatted message combining the person and quote
# Using an f-string for clean, readable string formatting
# The escaped quotes (\") properly enclose the quotation
message = f"{famous_person} once said, \"{quote}.\""

# Display the complete formatted message
print(message)

# This approach has several benefits:
# 1. The message variable can be reused multiple times
# 2. The formatting is separate from the printing
# 3. Makes the code more maintainable - change the format in one place
# 4. Easier to modify or add punctuation

# Alternative message formatting methods:
# message = famous_person + ' once said, "' + quote + '."'  # Using concatenation
# message = '{} once said, "{}"'.format(famous_person, quote)  # Using .format()