# 7. Python Program to Find Numbers Divisible by Another Number

def find_divisible_numbers(numbers, divisor):
    divisible_numbers = [num for num in numbers if num % divisor == 0]  # List comprehension to find divisible numbers
    return divisible_numbers

# Taking input from user
numbers = list(map(int, input("Enter a list of numbers (separated by spaces): ").split()))
divisor = int(input("Enter the divisor: "))

# Handling case when divisor is 0
if divisor == 0:
    print("Divisor cannot be zero.")
else:
    result = find_divisible_numbers(numbers, divisor)
    print(f"Numbers divisible by {divisor}: {result}")
