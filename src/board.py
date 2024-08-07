import numpy as np
import pygame

# Constants
BOARD_ROWS, BOARD_COLS = 3, 3
SQUARE_SIZE = 200  # Placeholder value; adjust based on your screen dimensions
CIRCLE_RADIUS = SQUARE_SIZE // 3
CROSS_WIDTH = 25

# Colors
BG_COLOR = (28, 170, 156)
LINE_COLOR = (23, 145, 135)
WHITE = (255, 255, 255)
CIRCLE_COLOR = (239, 231, 200)
CROSS_COLOR = (66, 66, 66)

class TicTacToe:
    def __init__(self, screen):
        self.screen = screen
        self.reset_game()

    def draw_lines(self):
        self.screen.fill(BG_COLOR)
        for row in range(1, BOARD_ROWS):
            pygame.draw.line(self.screen, LINE_COLOR, (0, row * SQUARE_SIZE), (self.screen.get_width(), row * SQUARE_SIZE), CROSS_WIDTH)
        for col in range(1, BOARD_COLS):
            pygame.draw.line(self.screen, LINE_COLOR, (col * SQUARE_SIZE, 0), (col * SQUARE_SIZE, self.screen.get_height()), CROSS_WIDTH)

    def mark_square(self, row, col, player):
        self.board[row][col] = player

    def available_square(self, row, col):
        return self.board[row][col] == 0

    @staticmethod
    def is_board_full(board):
        return not any(board[row][col] == 0 for row in range(3) for col in range(3))

    def draw_figures(self):
        for row in range(BOARD_ROWS):
            for col in range(BOARD_COLS):
                if self.board[row][col] == 1:
                    pygame.draw.line(self.screen, CROSS_COLOR, (col * SQUARE_SIZE + CROSS_WIDTH, row * SQUARE_SIZE + SQUARE_SIZE - CROSS_WIDTH), (col * SQUARE_SIZE + SQUARE_SIZE - CROSS_WIDTH, row * SQUARE_SIZE + CROSS_WIDTH), CROSS_WIDTH)
                    pygame.draw.line(self.screen, CROSS_COLOR, (col * SQUARE_SIZE + CROSS_WIDTH, row * SQUARE_SIZE + CROSS_WIDTH), (col * SQUARE_SIZE + SQUARE_SIZE - CROSS_WIDTH, row * SQUARE_SIZE + SQUARE_SIZE - CROSS_WIDTH), CROSS_WIDTH)
                elif self.board[row][col] == 2:
                    pygame.draw.circle(self.screen, CIRCLE_COLOR, (int(col * SQUARE_SIZE + SQUARE_SIZE // 2), int(row * SQUARE_SIZE + SQUARE_SIZE // 2)), CIRCLE_RADIUS, CROSS_WIDTH)

    @staticmethod
    def check_win(board, player):
        for row in range(BOARD_ROWS):
            if all(board[row][col] == player for col in range(BOARD_COLS)):
                return True
        for col in range(BOARD_COLS):
            if all(board[row][col] == player for row in range(BOARD_ROWS)):
                return True
        if all(board[row][row] == player for row in range(BOARD_ROWS)):
            return True
        if all(board[row][BOARD_COLS - row - 1] == player for row in range(BOARD_ROWS)):
            return True
        return False

    def draw_end_game(self, winner):
        font = pygame.font.Font(None, 90)
        if winner == 1:
            text = font.render('You win!', True, WHITE)
        elif winner == 2:
            text = font.render('AI wins!', True, WHITE)
        else:
            text = font.render('Draw!', True, WHITE)
        self.screen.blit(text, (self.screen.get_width() // 2 - text.get_width() // 2, self.screen.get_height() // 2 - text.get_height() // 2))
        pygame.display.update()
        pygame.time.delay(3000)

    def reset_game(self):
        self.board = np.zeros((BOARD_ROWS, BOARD_COLS))
        self.turn = 0
        self.game_over = False
        self.draw_lines()
        pygame.display.update()
