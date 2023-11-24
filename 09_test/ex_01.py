matrix = []
row_col = 3
for row in range(row_col):
    matrix.append([])
    for col in range(row_col):
        matrix[row].append(col + 1 + row * 3)
# row_col = 3
# matrix = [[(col+1 + row * 3) for col in range(row_col)] for row in range(row_col)]
print(*matrix, sep="\n")




# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9],
# ]





# my_list = [[1, 2, 3, 4], [5, 6, 7, 8], 9, [10, 11, 12]]
#
# print(my_list[1][0])

