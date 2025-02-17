# Demonstrating String Stripping Methods
# This program shows how to remove whitespace from strings using Python's strip methods

# Create a string with extra whitespace
# \t represents a tab character
# \n represents a newline character
name = "\tMajimba\t\n"
print(name)  # Shows the string with all whitespace visible

# lstrip() method - removes leading whitespace (from the left side)
print(name.lstrip())  # Removes the tab space before "Majimba"

# rstrip() method - removes trailing whitespace (from the right side)
print(name.rstrip())  # Removes the tab space and newline after "Majimba"

# strip() method - removes both leading and trailing whitespace
print(name.strip())   # Removes all surrounding whitespace

# Common use cases for stripping methods:
# - Cleaning user input
# - Processing data from files
# - Formatting text for display
# - Standardizing data

# Note: These methods return a new string; they don't modify the original
# The original 'name' variable still contains the whitespace
