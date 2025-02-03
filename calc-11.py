# 11. Python Program to Make a Simple Calculator

def calculator(a, b, operator):
    if operator == '+':
        return a + b
    elif operator == '-':
        return a - b
    elif operator == '*':
        return a * b
    elif operator == '/':
        if b != 0:
            return a / b
        else:
            return "Error: Division by zero"
    else:
        return "Invalid operator"
    
print("Simple Calculator")
a = float(input("Enter the first number: "))
b = float(input("Enter the second number: "))
operator = input("Enter an operator (+, -, *, /): ")
result = calculator(a, b, operator)
print(f"The result is: {result}")