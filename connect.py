def print_board(board):
    for row in board:
        print("|".join(row))
        print("-" * (4 * len(row) - 1))

def check_win(board, player):
    # Check horizontally
    for row in board:
        for col in range(len(row) - 3):
            if all(cell == player for cell in row[col:col + 4]):
                return True

    # Check vertically
    for col in range(len(board[0])):
        for row in range(len(board) - 3):
            if all(board[row + i][col] == player for i in range(4)):
                return True

    # Check diagonally (from top-left to bottom-right)
    for row in range(len(board) - 3):
        for col in range(len(board[0]) - 3):
            if all(board[row + i][col + i] == player for i in range(4)):
                return True

    # Check diagonally (from top-right to bottom-left)
    for row in range(len(board) - 3):
        for col in range(3, len(board[0])):
            if all(board[row + i][col - i] == player for i in range(4)):
                return True

    return False

def is_board_full(board):
    return all(cell != ' ' for row in board for cell in row)

def connect_four():
    # Initialize the game board
    board = [[' ' for _ in range(7)] for _ in range(6)]

    # Define players
    players = ['X', 'O']
    player_index = 0

    while True:
        print_board(board)

        # Get the current player's move
        column = int(input(f"Player {players[player_index]}, choose a column (1-7): ")) - 1

        # Check if the selected column is valid
        if 0 <= column < 7 and board[0][column] == ' ':
            # Drop the player's piece to the lowest available position in the selected column
            for row in range(5, -1, -1):
                if board[row][column] == ' ':
                    board[row][column] = players[player_index]
                    break

            # Check for a win
            if check_win(board, players[player_index]):
                print_board(board)
                print(f"Player {players[player_index]} wins!")
                break

            # Check for a tie
            if is_board_full(board):
                print_board(board)
                print("It's a tie!")
                break

            # Switch to the other player
            player_index = 1 - player_index
        else:
            print("Invalid move. Please choose a valid column.")

if __name__ == "__main__":
    connect_four()
