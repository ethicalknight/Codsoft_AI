import random

def print_board(board):
    for row in board:
        print("|".join(row))
        print("-" * 5)

def check_winner(board):
    for row in board:
        if row.count(row[0]) == 3 and row[0] != ' ':
            return True
    for col in range(3):
        if all(board[row][col] == board[0][col] and board[0][col] != ' ' for row in range(3)):
            return True
    if all(board[i][i] == board[0][0] and board[0][0] != ' ' for i in range(3)):
        return True
    if all(board[i][2 - i] == board[0][2] and board[0][2] != ' ' for i in range(3)):
        return True
    return False

def minimax(board, depth, is_maximizing):
    if check_winner(board):
        return -1 if is_maximizing else 1
    if all(cell != ' ' for row in board for cell in row):
        return 0

    if is_maximizing:
        best_score = -float('inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'O'
                    score = minimax(board, depth + 1, False)
                    board[i][j] = ' '
                    best_score = max(score, best_score)
        return best_score
    else:
        best_score = float('inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'X'
                    score = minimax(board, depth + 1, True)
                    board[i][j] = ' '
                    best_score = min(score, best_score)
        return best_score

def ai_move(board):
    best_score = -float('inf')
    move = (-1, -1)
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                board[i][j] = 'O'
                score = minimax(board, 0, False)
                board[i][j] = ' '
                if score > best_score:
                    best_score = score
                    move = (i, j)
    return move

def play_game():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    print("Welcome to Tic-Tac-Toe!")
    print_board(board)

    while True:
        row, col = map(int, input("Enter your move (row and column): ").split())
        if board[row][col] == ' ':
            board[row][col] = 'X'
            if check_winner(board):
                print_board(board)
                print("You win!")
                break
            if all(cell != ' ' for row in board for cell in row):
                print_board(board)
                print("It's a tie!")
                break
            print("AI is making a move...")
            ai_row, ai_col = ai_move(board)
            board[ai_row][ai_col] = 'O'
            if check_winner(board):
                print_board(board)
                print("AI wins!")
                break
            print_board(board)
        else:
            print("Invalid move. Try again.")

if __name__ == "__main__":
    play_game()
