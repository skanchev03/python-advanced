n = int(input())

matrix = []

for _ in range(n):
    row = list(input())
    matrix.append(row)

searched_symbol = input()

found = False

for row in range(n):
    for col in range(n):
        if matrix[row][col] == searched_symbol:
            print(f"({row}, {col})")
            found = True
            break
    if found:
        break

if not found:
    print(f"{searched_symbol} does not occur in the matrix")
