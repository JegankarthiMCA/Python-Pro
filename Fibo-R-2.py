# 2.Display the Fibonacci Sequence Using Recursion in Python Program?

def fibo(n, a=0, b=1):
    if n <= 0:  # Indented correctly
        return
    print(a, end=" ")  # Indented correctly
    fibo(n - 1, b, a + b)  # Recursive call

num = int(input("Enter the Number: "))
fibo(num)
