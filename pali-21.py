# 21. Python Program to Check Whether a String is Palindrome or Not

string = input("Enter a string: ")
if string == string[::-1]:
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")