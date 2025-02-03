# 6. Find the sum of Natural Number in using Recursion

def sum_of_natural_numbers(n):
    if n == 0:  # Base case
        return 0
    else:
        return n + sum_of_natural_numbers(n - 1)  # Recursive call

# Taking user input
number = int(input("Enter a positive integer: "))

# Handling negative input
if number < 0:
    print("Please enter a positive integer.")
else:
    result = sum_of_natural_numbers(number)
    print(f"The sum of the first {number} natural numbers is: {result}")
