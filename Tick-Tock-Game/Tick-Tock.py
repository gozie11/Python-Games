# How to play
# Starting with 'x', choose the position on the board using
# 't' (top), 'm' (middle), 'b' (bottom) for rows
# 'l' (left), 'm' (middle), 'r' (right) for columns

def print_board(board) :
    for row in board:
        print(" ".join(row))
    print("\n")

def check_win(board):
    # check rows, columns and diagonals for a win
    lines = [row for row in board] + [list(col) for col in zip(*board)]
    lines += [[board[i][i] for i in range(3)], [board[i][2-i] for i in range(3)]]
    for line in lines:
        if line == ['x', 'x', 'x']:
            return 'x'
        elif line == ['o','o', 'o']:
            return 'o'
    return None

def get_input(turn):
    while True:
        user_input = input(f"{turn} to move, choose a row (t,m,b) and column (l,m,r) like 'tl' or 'mm': ").lower()
        if len(user_input) == 2 and user_input[0] in 'tmb' and user_input[1] in 'lmr':
            row = {'t': 0, 'm': 1, 'b': 2}[user_input[0]]
            col = {'l': 0, 'm': 1, 'r': 2}[user_input[1]]
            if board[row][col] == '_':
                return row, col
        print("Invaild input or spot taken, try again.")

# Initialize game board
board = [['_', '_', '_'] for _ in range(3)]
turn = 'x'

# Main game loop
while True:
    print("Current board:")
    print_board(board)
    row, col = get_input(turn)
    board[row][col] = turn

    winner = check_win(board)
    if winner:
        print(f"{winner} wins!")
        print_board(board)
        break
    if all('_' not in row for row in board):
        print("It's a draw!")
        print_board(board)
        break

    turn = 'o' if turn == 'x' else 'x'
