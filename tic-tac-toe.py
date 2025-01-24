import pygame

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 600, 600
LINE_WIDTH = 15
CELL_SIZE = WIDTH // 3
BG_COLOR = (28, 170, 156)  # Teal
LINE_COLOR = (23, 145, 135)  # Grid lines
X_COLOR = (84, 84, 84)  # Dark gray
O_COLOR = (242, 235, 211)  # Beige

# Setup window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tic-Tac-Toe")

# Game state
board = [[None]*3 for _ in range(3)]
current_player = "X"
game_over = False

# Initialize font for text
font = pygame.font.Font(None, 74)


def draw_grid():
    # Vertical lines
    pygame.draw.line(screen, LINE_COLOR, (CELL_SIZE, 0),
                     (CELL_SIZE, HEIGHT), LINE_WIDTH)
    pygame.draw.line(screen, LINE_COLOR, (CELL_SIZE*2, 0),
                     (CELL_SIZE*2, HEIGHT), LINE_WIDTH)
    # Horizontal lines
    pygame.draw.line(screen, LINE_COLOR, (0, CELL_SIZE),
                     (WIDTH, CELL_SIZE), LINE_WIDTH)
    pygame.draw.line(screen, LINE_COLOR, (0, CELL_SIZE*2),
                     (WIDTH, CELL_SIZE*2), LINE_WIDTH)


def draw_symbols():
    for row in range(3):
        for col in range(3):
            symbol = board[row][col]
            if symbol:
                x = col * CELL_SIZE + CELL_SIZE//2
                y = row * CELL_SIZE + CELL_SIZE//2
                if symbol == "X":
                    # Draw X
                    pygame.draw.line(
                        screen, X_COLOR, (x-50, y-50), (x+50, y+50), LINE_WIDTH)
                    pygame.draw.line(
                        screen, X_COLOR, (x+50, y-50), (x-50, y+50), LINE_WIDTH)
                else:
                    # Draw O
                    pygame.draw.circle(screen, O_COLOR, (x, y), 50, LINE_WIDTH)


def check_winner():
    # Check rows and columns
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] and board[i][0]:
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] and board[0][i]:
            return board[0][i]
    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0]:
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2]:
        return board[0][2]
    return None


def check_draw():
    return all(cell is not None for row in board for cell in row)


def display_message(text):
    text_surface = font.render(text, True, (255, 255, 255))
    text_rect = text_surface.get_rect(center=(WIDTH//2, HEIGHT//2))
    screen.blit(text_surface, text_rect)


# Game loop
running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
            x, y = pygame.mouse.get_pos()
            row = y // CELL_SIZE
            col = x // CELL_SIZE

            if board[row][col] is None:
                board[row][col] = current_player
                current_player = "O" if current_player == "X" else "X"

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:  # Reset game
                board = [[None]*3 for _ in range(3)]
                current_player = "X"
                game_over = False

    # Update game state
    winner = check_winner()
    if winner:
        game_over = True
    elif check_draw():
        game_over = True

    # Draw everything
    screen.fill(BG_COLOR)
    draw_grid()
    draw_symbols()

    if game_over:
        if winner:
            display_message(f"Player {winner} wins!")
        else:
            display_message("Game Draw!")

    pygame.display.update()
    clock.tick(60)

pygame.quit()
