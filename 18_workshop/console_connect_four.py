SLOTS_TO_WIN = 4
ROWS = 6
COLS = 7


class InvalidColumnError(Exception):
    pass


class FullColumnError(Exception):
    pass


def create_board(rows: int, cols: int):
    return [[0 for _ in range(cols)] for _ in range(rows)]


def print_board(game_board: list):
    for row in game_board:
        print(row)


def validate_player_column(player_col: int, max_col: int):
    if not (0 <= player_col < max_col):
        raise InvalidColumnError


def place_player_choice(game_board: list, col: int, player_num: int):
    for row in range(len(game_board) -1, -1, -1):
        if game_board[row][col] == 0:
            game_board[row][col] = player_num
            return row, col
    raise FullColumnError


def is_player(game_board: list, row: int, col: int, player_num: int):
    try:
        return game_board[row][col] == player
    except IndexError:
        return False



def check_for_winner_row(game_board: list, row: int, col: int, player_num: int, slots: int):
    filled = 1

    for i in range(1, slots):
        if is_player(game_board, row, col + i, player_num):
            filled += 1
        else:
            break

    for i in range(1, slots):
        if is_player(game_board, row, col - i, player_num):
            filled += 1
        else:
            break

    return filled >= slots


def check_for_winner_col(game_board: list, row: int, col: int, player_num: int, slots: int):
    return all([is_player(game_board, row + i, col, player_num) for i in range(slots)])

def check_for_winner_diagonal(game_board: list, row: int, col: int, player_num: int, slots: int):
    filled = 1

    for i in range(1, slots):
        if is_player(game_board, row - i, col + i, player_num):
            filled += 1
        else:
            break

    for i in range(1, slots):
        if is_player(game_board, row + i, col - i, player_num):
            filled += 1
        else:
            break
    if filled >= slots:
        return True

    filled = 1

    for i in range(1, slots):
        if is_player(game_board, row + i, col + i, player_num):
            filled += 1
        else:
            break

    for i in range(1, slots):
        if is_player(game_board, row - i, col - i, player_num):
            filled += 1
        else:
            break

    return filled >= slots


def check_for_winner(game_board: list, row: int, col: int, player_num: int, slots = SLOTS_TO_WIN):
    winner_row = check_for_winner_row(game_board, row, col, player_num, slots)
    winner_col = check_for_winner_col(game_board, row, col, player_num, slots)
    winner_diagonal = check_for_winner_diagonal(game_board, row, col, player_num, slots)

    if winner_row or winner_col or winner_diagonal:
        return True
    return False


board = create_board(ROWS, COLS)
print_board(board)
player = 1
turns = 1

while True:
    try:
        player_column = int(input(f"Player {player}, please choose a column: ")) - 1
        validate_player_column(player_column, COLS)
        current_row, current_col = place_player_choice(board, player_column, player)
        print_board(board)
        if check_for_winner(board, current_row, current_col, player):
            print(f"Player {player} won!")
            break
    except InvalidColumnError:
        print("Please enter a valid number, between 1 and 7!")
        continue
    except FullColumnError:
        print("This column is full! Select another one!")
        continue
    except ValueError:
        print("Please enter a valid number!")
        continue

    if ROWS * COLS == turns:
        print("Draw!")
        break

    turns += 1
    player = 2 if player == 1 else 1
