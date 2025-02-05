board = [[' ', ' ', ' '],
         [' ', ' ', ' '],
         [' ', ' ', ' ']]


def greet_user():
    print("Vítejte ve hře Tic-tac-toe!")
    print("Cílem hry je umístit tři své symboly vedle sebe v řadě, sloupci nebo diagonále.")
    print("Hru začíná hráč s kolečky.")
    print("Hru ukončíte stisknutím klávesy q.")

def print_board(board):
    print('-' * 5)
    for row in board:
        print('|'.join(row))
        print('-' * 5)


def check_winner(board, player):
    # Check rows, columns and diagonals for a win
    for row in board:
        if all(s == player for s in row):
            return True
    for col in range(3):
        if all(row[col] == player for row in board):
            return True
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    return False


def is_full(board):
    return all(all(cell != " " for cell in row) for row in board)


def get_move(player):
    while True:
        move = input(f"Hráč {player}, zadejte pozici (1-9) nebo 'q' pro ukončení: ")
        if move.lower() == 'q':
            print("Hra ukončena.")
            exit()
        try:
            move = int(move) - 1
            if move < 0 or move >= 9:
                print("Neplatná pozice. Zadejte číslo od 1 do 9.")
            else:
                return move
        except ValueError:
            print("Neplatný vstup. Zadejte číslo od 1 do 9.")


def main():
    greet_user()

    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"

    while True:
        print_board(board)
        move = get_move(current_player)
        row, col = divmod(move, 3)

        if board[row][col] != " ":
            print("Pole je obsazené. Zvolte jiné pole.")
            continue

        board[row][col] = current_player

        if check_winner(board, current_player):
            print_board(board)
            print(f"Hráč {current_player} vyhrál!")
            break

        if is_full(board):
            print_board(board)
            print("Remíza!")
            break

        current_player = "O" if current_player == "X" else "X"


if __name__ == "__main__":
    main()

