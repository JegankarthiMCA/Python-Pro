# 1.Find the Factorial of Number Using Recursion in Python Program?


def factorial(n):
    if n==1:
        return 1
    else:
        return n * factorial(n - 1)
    
num = int(input("Enter the Value : "))
    
result = factorial(num)
    
print(f"Factorial of {num} is {result}")