rows = int(input())

matrix = []

for _ in range(rows):
    row = [int(x) for x in input().split(", ")]
    matrix.append(row)

flattened_matrix = []

for row in matrix:
    for num in row:
        flattened_matrix.append(num)

print(flattened_matrix)
