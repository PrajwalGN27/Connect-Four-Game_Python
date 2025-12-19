#                     Connect Four Game
import random
print("Connect Four Game")
print("-----------------")
possibles=["A","B","C","D","E","F","G"]
board=[[" " for _ in range(7)] for _ in range(6)]

rows=6  
cols=7

def print_board():
    print("  A   B   C   D   E   F   G")
    print("+---+---+---+---+---+---+---+")
    for row in board:
        print("| " + " | ".join(row) + " |")
        print("+---+---+---+---+---+---+---+")
    print()
def check_winner(player):
    for r in range(rows):
        for c in range(cols - 3):
            if all(board[r][c + i] == player for i in range(4)):
                return True
    for c in range(cols):
        for r in range(rows - 3):
            if all(board[r + i][c] == player for i in range(4)):
                return True
    for r in range(rows - 3):
        for c in range(cols - 3):
            if all(board[r + i][c + i] == player for i in range(4)):
                return True
    for r in range(3, rows):
        for c in range(cols - 3):
            if all(board[r - i][c + i] == player for i in range(4)):
                return True
    return False
def is_full():
    return all(board[0][c] != " " for c in range(cols))
def make_move(col, player):
    for r in range(rows - 1, -1, -1):
        if board[r][col] == " ":
            board[r][col] = player
            return True
    return False
def get_computer_move():
    available_cols = [c for c in range(cols) if board[0][c] == " "]
    return random.choice(available_cols) if available_cols else None

print_board()
while True:
    player_move = input("Player 1 (X), choose a column (A-G): ").upper()
    if player_move not in possibles:
        print("Invalid column. Choose A-G.")
        continue
    col = possibles.index(player_move)
    if not make_move(col, "X"):
        print("Column full. Choose another.")
        continue
    print_board()
    if check_winner("X"):
        print("Player 1 (X) wins!")
        break
    if is_full():
        print("It's a draw!")
        break
    comp_col = get_computer_move()
    if comp_col is not None:
        make_move(comp_col, "O")
        print(f"Computer (O) chooses column {possibles[comp_col]}")
        print_board()
        if check_winner("O"):
            print("Computer (O) wins!")
            break
        if is_full():
            print("It's a draw!")
            break
    else:
        print("It's a draw!")
        break

