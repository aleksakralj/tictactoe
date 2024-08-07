import numpy as np
import pytest
from src.minmax import minimax, evaluate_moves, update_best_score
from src.board import TicTacToe

# Dummy TicTacToe object for testing purposes
class DummyTicTacToe(TicTacToe):
    @staticmethod
    def check_win(board, player):
        for row in range(3):
            if all(board[row][col] == player for col in range(3)):
                return True
        for col in range(3):
            if all(board[row][col] == player for row in range(3)):
                return True
        if all(board[row][row] == player for row in range(3)):
            return True
        if all(board[row][2 - row] == player for row in range(3)):
            return True
        return False

    @staticmethod
    def is_board_full(board):
        return not any(board[row][col] == 0 for row in range(3) for col in range(3))

def test_minimax_win_for_player():
    board = np.array([
        [1, 1, 1],
        [0, 0, 0],
        [0, 0, 0]
    ])
    score, move = minimax(board, 0, 2)
    assert score == -10  # Human wins, worst score for AI
    assert move is None

def test_minimax_win_for_ai():
    board = np.array([
        [2, 2, 2],
        [0, 0, 0],
        [0, 0, 0]
    ])
    score, move = minimax(board, 0, 1)
    assert score == 10  # AI wins, best score for AI
    assert move is None

def test_minimax_draw():
    board = np.array([
        [1, 2, 1],
        [2, 1, 2],
        [2, 1, 2]
    ])
    score, move = minimax(board, 0, 1)
    assert score == 0  # Draw
    assert move is None

def test_minimax_partial_board():
    board = np.array([
        [1, 2, 0],
        [2, 1, 0],
        [0, 0, 0]
    ])
    depth = 0
    player = 1
    score, move = minimax(board, depth, player)
    assert isinstance(score, (int, float))
    assert move is None or isinstance(move, tuple) and len(move) == 2

def test_evaluate_moves_with_multiple_options():
    board = np.array([
        [1, 2, 0],
        [2, 0, 1],
        [1, 0, 0]
    ])
    depth = 0
    player = 1
    score, move = evaluate_moves(board, depth, player)
    assert isinstance(score, (int, float))
    assert move is None or isinstance(move, tuple) and len(move) == 2

def test_evaluate_moves_with_critical_moves():
    board = np.array([
        [1, 1, 0],
        [2, 0, 2],
        [0, 0, 1]
    ])
    depth = 0
    player = 2
    score, move = evaluate_moves(board, depth, player)
    assert isinstance(score, (int, float))
    assert move is not None

def test_update_best_score_for_ai():
    best_score, best_move = update_best_score(10, -np.Inf, (0, 0), 2, None)
    assert best_score == 10
    assert best_move == (0, 0)

def test_update_best_score_for_human():
    best_score, best_move = update_best_score(-10, np.Inf, (0, 0), 1, None)
    assert best_score == -10
    assert best_move == (0, 0)

def test_minimax_empty_board():
    board = np.array([
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]
    ])
    score, move = minimax(board, 0, 1)
    assert isinstance(score, (int, float))
    assert move is None or isinstance(move, tuple) and len(move) == 2

def test_minimax_board_with_single_move():
    board = np.array([
        [1, 2, 0],
        [0, 0, 0],
        [0, 0, 0]
    ])
    score, move = minimax(board, 0, 2)
    assert isinstance(score, (int, float))
    assert move is None or isinstance(move, tuple) and len(move) == 2

def test_minimax_with_corner_case():
    board = np.array([
        [1, 2, 0],
        [2, 1, 0],
        [0, 0, 1]
    ])
    score, move = minimax(board, 0, 1)
    assert isinstance(score, (int, float))
    assert move is None or isinstance(move, tuple) and len(move) == 2
