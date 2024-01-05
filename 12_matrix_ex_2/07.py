rows, cols = map(int, input().split(', '))

matrix = []

for row in range(rows):
    matrix.append(input().split(', '))

searched_symbol = input()

for r in range(rows):
    for c in range(cols):
        if searched_symbol == matrix[r][c]:
            print(f"{r}, {c}")