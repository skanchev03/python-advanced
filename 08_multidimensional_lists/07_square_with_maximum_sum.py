rows, cols = [int(x) for x in input().split(", ")]

matrix = []

for _ in range(rows):
    row = [int(x) for x in input().split(", ")]
    matrix.append(row)

max_sum = float('-inf')
max_matrix = []

for row in range(rows-1):
    for col in range(cols-1):
        current_matrix = [
            matrix[row][col], matrix[row][col + 1],
            matrix[row + 1][col], matrix[row + 1][col + 1]
        ]
        current_sum = sum(current_matrix)

        if current_sum > max_sum:
            max_sum = current_sum
            max_matrix = current_matrix

print(f"{max_matrix[0]} {max_matrix[1]}")
print(f"{max_matrix[2]} {max_matrix[3]}")
print(max_sum)
