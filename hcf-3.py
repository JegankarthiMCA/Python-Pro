# 3.Find the HCF or GCD?


def hcf(a, b):
    a, b = abs(a), abs(b)  # Convert to absolute values to handle negative numbers
    if b == 0:
        return a
    else:
        return hcf(b, a % b)

num1 = int(input("Enter the First Number: "))
num2 = int(input("Enter the Second Number: "))

result = hcf(num1, num2)

print(f"The HCF/GCD of {num1} & {num2} is {result}")
