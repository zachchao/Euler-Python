import re


matrix = []
with open("Problem345.txt", "r") as f:
	lines = f.readlines()
	for line in lines:
		values = [int(i) for i in re.findall("[0-9]+", line)]
		matrix.append(values)

#Transpose the matrix
#Empty array to write to
matrixTranspose = [[0 for i in range(len(matrix))] for j in range(len(matrix[0]))]
for row in range(len(matrix)):
	for column in range(len(matrix[0])):
		matrixTranspose[column][row] = matrix[row][column]

matrixSum = 0
for row in matrixTranspose:
	print(row)
	matrixSum += max(row)
	print(max(row))

print(matrixSum)

