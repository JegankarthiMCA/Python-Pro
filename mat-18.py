# 18. Python Program to Add Two Matrices

# Input the number of rows and columns
rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

# Initialize matrices
matrix1 = []
matrix2 = []

# Input elements of the first matrix
print("Enter elements of the first matrix:")
for i in range(rows):
    row = list(map(int, input().split()))
    matrix1.append(row)

# Input elements of the second matrix
print("Enter elements of the second matrix:")
for i in range(rows):
    row = list(map(int, input().split()))
    matrix2.append(row)

# Initialize result matrix
result = []

# Add the matrices
for i in range(rows):
    result_row = []
    for j in range(cols):
        result_row.append(matrix1[i][j] + matrix2[i][j])
    result.append(result_row)

# Display the result matrix
print("The sum of the matrices is:")
for row in result:
    print(row)
