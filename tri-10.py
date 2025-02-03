# 10. Python Program to Calculate the Area of a Triangle

import math
def herons_area(a, b, c):
        s = (a + b + c) / 2
        return math.sqrt(s * (s - a) * (s - b) * (s - c))

a = float(input("Enter the first side of the triangle: "))
b = float(input("Enter the second side of the triangle: "))
c = float(input("Enter the third side of the triangle: "))
    
if a + b > c and a + c > b and b + c > a:
    area = herons_area(a, b, c)
    print(f"The area of the triangle is: {area}")
else:
    print("The given sides do not form a valid triangle.")