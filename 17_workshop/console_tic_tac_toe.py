def print_board(game_board: list):
    for r in board:
        print(f"| {' | '.join(r)} |")


def check_for_winner_row(game_board: list, sign: str):
    for r in game_board:
        if r.count(sign) == 3:
            return True
    return False


def check_for_winner_col(game_board: list, sign: str):
    for c in range(len(game_board)):
        sign_counter = 0
        for r in range(len(game_board)):
            if game_board[r][c] == sign:
                sign_counter += 1
        if sign_counter == 3:
            return True
    return False


def check_for_winner_diagonal(game_board: list, sign: str):
    primary_counter = 0
    secondary_counter = 0

    for i in range(len(game_board)):
        if board[i][i] == sign:
            primary_counter += 1
        if board[i][len(game_board) - i - 1] == sign:
            secondary_counter += 1

    if primary_counter == 3 or secondary_counter == 3:
        return True
    return False


def check_for_winner(game_board: list, sign: str):
    winner_row = check_for_winner_row(game_board, sign)
    winner_col = check_for_winner_col(game_board, sign)
    winner_diagonal = check_for_winner_diagonal(game_board, sign)

    if winner_row or winner_col or winner_diagonal:
        return True
    return False


player_one_name = input("Player one name: ")
player_two_name =input("Player two name: ")
player_one_sign = input(f"{player_one_name} would you like to play with 'X' or 'O'? ")

while player_one_sign not in ("X", "O"):
    print("Please enter either 'X' or 'O'.")
    player_one_sign = input(f"{player_one_name} would you like to play with 'X' or 'O'? ")

player_two_sign = "O" if player_one_sign == "X" else "X"

print("This is the numeration of the board:")
print("| 1 | 2 | 3 |")
print("| 4 | 5 | 6 |")
print("| 7 | 8 | 9 |")

print(f"{player_one_name} starts first!")

turn = 1
board = [[" ", " ", " "],
         [" ", " ", " "],
         [" ", " ", " "]]
mapper = {
    1: (0, 0),
    2: (0, 1),
    3: (0, 2),
    4: (1, 0),
    5: (1, 1),
    6: (1, 2),
    7: (2, 0),
    8: (2, 1),
    9: (2, 2),
}


while True:
    current_player = player_one_name if turn % 2 != 0 else player_two_name
    current_sign = player_one_sign if turn % 2 != 0 else player_two_sign

    try:
        position = int(input(f"{current_player} please choose a free position between [1-9]: "))
    except ValueError:
        print("Please enter a valid number!")
        continue

    if not (1 <= position <= 9):
        print("Please enter a valid number, between 1 and 9!")
        continue

    row, col = mapper[position]

    if board[row][col] != " ":
        print("This position is already occupied.")
        continue

    board[row][col] = current_sign
    print_board(board)
    if turn >= 5 and check_for_winner(board, current_sign):
        print(f"{current_player} won!")
        break

    if turn == 9:
        print("Draw!")
        break

    turn += 1
