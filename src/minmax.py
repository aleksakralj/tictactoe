import numpy as np

from src.board import TicTacToe

def minimax(board, depth, player):
    if TicTacToe.check_win(board, 1):
        return -10 + depth, None  # Human wins, worst score for AI
    elif TicTacToe.check_win(board, 2):
        return 10 - depth, None  # AI wins, best score for AI
    elif TicTacToe.is_board_full(board):
        return 0, None  # Draw, neutral score

    return evaluate_moves(board, depth, player)


def evaluate_moves(board, depth, player):
    best_score = -np.Inf if player == 2 else np.Inf
    best_move = None
    
    for row in range(3):
        for col in range(3):
            if board[row][col] == 0:
                board[row][col] = player
                score, _ = minimax(board, depth + 1, 1 if player == 2 else 2)
                board[row][col] = 0
                best_score, best_move = update_best_score(score, best_score, (row, col), player, best_move)
    
    return best_score, best_move

def update_best_score(score, best_score, move, player, best_move):
    if player == 2:  # AI's turn
        if score > best_score:
            return score, move
    else:  # Human's turn
        if score < best_score:
            return score, move
    return best_score, best_move
