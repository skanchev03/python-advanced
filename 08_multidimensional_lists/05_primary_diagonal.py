n = int(input())

matrix = []

for _ in range(n):
    row = [int(x) for x in input().split()]
    matrix.append(row)

diagonal_sum = 0

for i in range(n):
    diagonal_sum += matrix[i][i]

print(diagonal_sum)
