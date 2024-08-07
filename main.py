import time
import pygame
import sys
from src.board import TicTacToe
from src.minmax import minimax

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 600, 600
SQUARE_SIZE = min(WIDTH // 3, HEIGHT // 3)

# Initialize the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tic Tac Toe")

# Create a TicTacToe instance
game = TicTacToe(screen)

def handle_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            game.reset_game()

def handle_player_move():
    if pygame.mouse.get_pressed()[0]:
        mouse_x, mouse_y = pygame.mouse.get_pos()
        if mouse_x < 3 * SQUARE_SIZE and mouse_y < (3 * SQUARE_SIZE):
            clicked_row = int(mouse_y // SQUARE_SIZE)
            clicked_col = int(mouse_x // SQUARE_SIZE)
            if game.available_square(clicked_row, clicked_col):
                game.mark_square(clicked_row, clicked_col, 1)
                game.draw_figures()
                return True
    return False

def ai_move():
    if game.turn != 1:
        time.sleep(0.5)
    if game.turn < 9:
        _, best_move = minimax(game.board, 0, 2)
        if best_move:
            row, col = best_move
            game.mark_square(row, col, 2)
            return True
    return False

def check_game_status():
    if TicTacToe.check_win(game.board, 1):
        game.draw_end_game(1)
        game.game_over = True
    elif TicTacToe.check_win(game.board, 2):
        game.draw_end_game(2)
        game.game_over = True
    elif TicTacToe.is_board_full(game.board):
        game.draw_end_game(None)
        game.game_over = True

def main():
    while True:
        handle_events()
        
        if not game.game_over and handle_player_move():
            game.turn += 1
            if not game.game_over and ai_move():
                game.draw_figures()
                game.turn += 1
            check_game_status()

        pygame.display.update()

if __name__ == "__main__":
    main()
