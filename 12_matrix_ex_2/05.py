row_col = int(input())
matrix = []

for row in range(row_col):
    element_matrix = [int(x) for x in input().split(', ')]
    matrix.append(element_matrix)

diagonal_sum = sum(matrix[i][i] for i in range(row_col))
secondary_diagonal_sum = sum(matrix[i][row_col - 1 - i] for i in range(row_col))

print(diagonal_sum)
print(secondary_diagonal_sum)