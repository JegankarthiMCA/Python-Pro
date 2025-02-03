# 4.Find the LCM?

def hcf(x, y):
    if y == 0:  # Proper indentation
        return x
    else:
        return hcf(y, x % y)

def lcm(x, y):
    return abs(x * y) // hcf(x, y)  # Using absolute values for safety

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

result = lcm(num1, num2)

print(f"The LCM of {num1} and {num2} is {result}")
