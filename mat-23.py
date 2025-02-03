# 23. Python Program to Transpose a Matrix

# Input the number of rows and columns
rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

# Initialize the matrix
matrix = []

# Input elements of the matrix
print("Enter elements of the matrix:")
for i in range(rows):
    row = list(map(int, input().split()))
    matrix.append(row)

# Calculate the transpose of the matrix
transpose = [[matrix[j][i] for j in range(rows)] for i in range(cols)]

# Output the transposed matrix
print("Transposed matrix:")
for row in transpose:
    print(row)
