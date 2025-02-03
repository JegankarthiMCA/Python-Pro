# 1.Find the Factorial of Number Using Recursion in Python Program?


def factorial(a):
    if a == 0 or a == 1:  # Base case for 0 and 1
        return 1
    else:
        return a * factorial(a - 1)

val = int(input("Enter any Factorial number value: "))

if val < 0:
    print("Factorial is not defined for negative numbers.")
else:
    result = factorial(val)
    print(f"Factorial of {val} is {result}")
