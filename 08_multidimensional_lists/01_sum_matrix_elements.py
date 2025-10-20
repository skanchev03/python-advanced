rows, cols = [int(x) for x in input().split(", ")]

matrix = []

for _ in range(rows):
    row = [int(x) for x in input().split(", ")]
    matrix.append(row)

total_sum = 0

for row in matrix:
    for num in row:
        total_sum += num

print(total_sum)
print(matrix)
