row_col = int(input())

matrix = []

for row in range(row_col):
    current_row = input().split(", ")
    matrix.append(current_row)

for r in matrix:
    print(*r, sep=", ")

# print(*[input().split(", ") for row in range(int(input()))], sep="\n")