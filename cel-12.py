# 12. Python Program to Convert Celsius to Fahrenheit

def celsius_to_fahrenheit(celsius):

    return (celsius * 9/5) + 32

celsius = float(input("Enter the temperature in Celsius: "))

fahrenheit = celsius_to_fahrenheit(celsius)

print(f"{celsius}° Celsius is equal to {fahrenheit}° Fahrenheit")