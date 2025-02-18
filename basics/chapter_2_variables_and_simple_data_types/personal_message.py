# Program: Personal Message
# Author: Chawana Maseka
# Date: February 18, 2025
# Description: Creates and displays a personalized message using string variables

# Creating personalized messages with f-strings
# This example combines:
# 1. Variable assignment
# 2. f-string formatting
# 3. The title() method for proper name capitalization

name = "Majimba"  # Store the name in a variable
# Create a personalized message using an f-string
# The name.title() ensures the name starts with a capital letter
message = f"Hello {name.title()}, would you like to learn some Python today?"
print(message)  # Display the personalized message

# This is a common pattern in real programs:
# - Store user data in variables
# - Format it appropriately
# - Create personalized output