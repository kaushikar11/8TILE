import pygame
import sys
import random

# Initialize pygame
pygame.init()

# Constants
TILE_SIZE = 100
BOARD_SIZE = 3
WINDOW_SIZE = TILE_SIZE * BOARD_SIZE
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)

# Function to draw the board
def draw_board(screen, puzzle):
    screen.fill(BLACK)
    for i in range(9):
        row, col = i // 3, i % 3
        x, y = col * TILE_SIZE, row * TILE_SIZE
        value = puzzle[i]
        if value != 0:
            pygame.draw.rect(screen, WHITE, (x, y, TILE_SIZE, TILE_SIZE))
            font = pygame.font.Font(None, 74)
            text = font.render(str(value), True, BLACK)
            screen.blit(text, (x + 30, y + 30))
        else:
            pygame.draw.rect(screen, GRAY, (x, y, TILE_SIZE, TILE_SIZE))
    pygame.display.flip()

# Function to handle key presses
def handle_keypress(key, puzzle):
    zero_pos = puzzle.index(0)  # find the position of the blank tile
    row, col = zero_pos // 3, zero_pos % 3

    if key == pygame.K_UP and row < 2:
        new_zero_pos = zero_pos + 3
    elif key == pygame.K_DOWN and row > 0:
        new_zero_pos = zero_pos - 3
    elif key == pygame.K_LEFT and col < 2:
        new_zero_pos = zero_pos + 1
    elif key == pygame.K_RIGHT and col > 0:
        new_zero_pos = zero_pos - 1
    else:
        return

    # Swap tiles
    puzzle[zero_pos], puzzle[new_zero_pos] = puzzle[new_zero_pos], puzzle[zero_pos]

# Main function
def main():
    # Set up display
    screen = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE))
    pygame.display.set_caption("8-Puzzle Game")

    # Define initial puzzle configuration (randomize)
    puzzle = [1, 2, 3, 4, 5, 6, 7, 8, 0]
    random.shuffle(puzzle)

    # Main game loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                handle_keypress(event.key, puzzle)

        # Clear screen and draw the board
        draw_board(screen, puzzle)

if __name__ == "__main__":
    main()
