n = int(input())

grid = []

for _ in range(n):
    row = list(input())
    grid.append(row)

total_stars = 0
pac_row = 0
pac_col = 0

for row in range(n):
    for col in range(n):
        if grid[row][col] == "P":
            pac_row = row
            pac_col = col
        if grid[row][col] == "*":
            total_stars += 1

health = 100
immune = False
collected_stars = 0

moves = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}

while True:
    command = input()

    if command == "end":
        break

    row_move, col_move = moves[command]

    pac_row = (pac_row + row_move) % n
    pac_col = (pac_col + col_move) % n

    current_cell = grid[pac_row][pac_col]

    if current_cell == "*":
        collected_stars += 1
    elif current_cell == "G":
        if immune:
            immune = False
        else:
            health -= 50
    elif current_cell == "F":
        immune = True

    for row in range(n):
        for col in range(n):
            if grid[row][col] == "P":
                grid[row][col] = "-"

    grid[pac_row][pac_col] = "P"

    if health <= 0:
        break

    if collected_stars == total_stars:
        break

if health <= 0:
    print(f"Game over! Pacman last coordinates [{pac_row},{pac_col}]")
elif collected_stars == total_stars:
    print("Pacman wins! All the stars are collected.")
else:
    print("Pacman failed to collect all the stars.")

print(f"Health: {health}")
if collected_stars < total_stars:
    print(f"Uncollected stars: {total_stars - collected_stars}")

for row in grid:
    print("".join(row))
