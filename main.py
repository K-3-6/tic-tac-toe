def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_win(board, player):
    for i in range(3):
        if all([cell == player for cell in board[i]]) or all([board[j][i] == player for j in range(3)]):
            return True
    if all([board[i][i] == player for i in range(3)]) or all([board[i][2 - i] == player for i in range(3)]):
        return True
    return False

def is_draw(board):
    return all([cell in ['X', 'O'] for row in board for cell in row])

def play_game():
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"

    while True:
        print_board(board)
        print(f"Ruch gracza {current_player}")
        try:
            row = int(input("Podaj wiersz (0-2): "))
            col = int(input("Podaj kolumnę (0-2): "))
        except ValueError:
            print("Nieprawidłowy format danych. Podaj liczby całkowite.")
            continue

        if 0 <= row <= 2 and 0 <= col <= 2 and board[row][col] == " ":
            board[row][col] = current_player
            if check_win(board, current_player):
                print_board(board)
                print(f"Gracz {current_player} wygrał!")
                break
            elif is_draw(board):
                print_board(board)
                print("Remis!")
                break
            current_player = "O" if current_player == "X" else "X"
        else:
            print("Nieprawidłowy ruch. Spróbuj ponownie.")

if __name__ == "__main__":
    play_game()
