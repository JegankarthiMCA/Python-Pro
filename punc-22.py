# 22. Python Program to Remove Punctuations from a String

import string

# Input string from the user
string_input = input("Enter a string: ")

# Remove punctuation using translate and maketrans
cleaned_string = string_input.translate(str.maketrans('', '', string.punctuation))

# Output the string without punctuation
print("String without punctuation:", cleaned_string)
