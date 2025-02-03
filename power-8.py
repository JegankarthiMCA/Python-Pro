# 8. Python Program to Display Powers of 2 Using Anonymous Function

# Take input from user
n = int(input("Enter the number of terms: "))

# Print the powers of 2 using a lambda function
print("Powers of 2:")

# Using lambda to compute powers of 2
power_of_2 = lambda x: 2 ** x

for i in range(n):
    print(f"2^{i} = {power_of_2(i)}")
