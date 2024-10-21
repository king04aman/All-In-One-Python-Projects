import pygame
import sys
import numpy as np

pygame.init()

WIDTH, HEIGHT = 600, 600
LINE_WIDTH = 15
BOARD_ROWS = 3
BOARD_COLS = 3
SQUARE_SIZE = WIDTH // BOARD_COLS
CIRCLE_RADIUS = SQUARE_SIZE // 3
CIRCLE_WIDTH = 15
CROSS_WIDTH = 25
SPACE = SQUARE_SIZE // 4

BG_COLOR = (28, 170, 156)
LINE_COLOR = (23, 145, 135)
CIRCLE_COLOR = (239, 231, 200)
CROSS_COLOR = (66, 66, 66)
TEXT_COLOR = (255, 255, 255)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Tic Tac Toe')
screen.fill(BG_COLOR)

font = pygame.font.Font(None, 40)  # Font for displaying messages
board = np.zeros((BOARD_ROWS, BOARD_COLS))

difficulty = "medium"  # AI difficulty level ("easy", "medium", "hard")

def draw_lines():
    for row in range(1, BOARD_ROWS):
        pygame.draw.line(screen, LINE_COLOR, (0, row * SQUARE_SIZE), (WIDTH, row * SQUARE_SIZE), LINE_WIDTH)
    for col in range(1, BOARD_COLS):
        pygame.draw.line(screen, LINE_COLOR, (col * SQUARE_SIZE, 0), (col * SQUARE_SIZE, HEIGHT), LINE_WIDTH)

# Draw figures (O and X)
def draw_figures():
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            if board[row][col] == 1:
                pygame.draw.circle(screen, CIRCLE_COLOR,
                                   (int(col * SQUARE_SIZE + SQUARE_SIZE // 2), int(row * SQUARE_SIZE + SQUARE_SIZE // 2)),
                                   CIRCLE_RADIUS, CIRCLE_WIDTH)
            elif board[row][col] == 2:
                pygame.draw.line(screen, CROSS_COLOR,
                                 (col * SQUARE_SIZE + SPACE, row * SQUARE_SIZE + SQUARE_SIZE - SPACE),
                                 (col * SQUARE_SIZE + SQUARE_SIZE - SPACE, row * SQUARE_SIZE + SPACE), CROSS_WIDTH)
                pygame.draw.line(screen, CROSS_COLOR,
                                 (col * SQUARE_SIZE + SPACE, row * SQUARE_SIZE + SPACE),
                                 (col * SQUARE_SIZE + SQUARE_SIZE - SPACE, row * SQUARE_SIZE + SQUARE_SIZE - SPACE),
                                 CROSS_WIDTH)

def mark_square(row, col, player):
    board[row][col] = player

def available_square(row, col):
    return board[row][col] == 0

def is_board_full():
    return np.all(board != 0)

def check_win(player):
    for row in range(BOARD_ROWS):
        if np.all(board[row, :] == player):
            return True
    for col in range(BOARD_COLS):
        if np.all(board[:, col] == player):
            return True
    if board[0, 0] == player and board[1, 1] == player and board[2, 2] == player:
        return True
    if board[0, 2] == player and board[1, 1] == player and board[2, 0] == player:
        return True
    return False

def display_message(message):
    text = font.render(message, True, TEXT_COLOR)
    text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
    screen.blit(text, text_rect)
    pygame.display.update()
    pygame.time.wait(2000)  # Wait for 2 seconds to display the message

# Minimax algorithm with difficulty levels
def minimax(board, depth, is_maximizing):
    if check_win(2):  # AI win
        return 1
    elif check_win(1):  # Player win
        return -1
    elif is_board_full():
        return 0

    if is_maximizing:
        best_score = -np.inf
        for row in range(BOARD_ROWS):
            for col in range(BOARD_COLS):
                if available_square(row, col):
                    board[row][col] = 2
                    score = minimax(board, depth + 1, False)
                    board[row][col] = 0
                    best_score = max(score, best_score)
        return best_score
    else:
        best_score = np.inf
        for row in range(BOARD_ROWS):
            for col in range(BOARD_COLS):
                if available_square(row, col):
                    board[row][col] = 1
                    score = minimax(board, depth + 1, True)
                    board[row][col] = 0
                    best_score = min(score, best_score)
        return best_score

# AI Move based on difficulty level
def ai_move():
    best_score = -np.inf
    move = None
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            if available_square(row, col):
                board[row][col] = 2
                score = minimax(board, 0, False)
                board[row][col] = 0
                if score > best_score:
                    best_score = score
                    move = (row, col)
    
    if move:
        mark_square(move[0], move[1], 2)

# Easy AI move: choose a random available square
def easy_ai_move():
    available_moves = [(row, col) for row in range(BOARD_ROWS) for col in range(BOARD_COLS) if available_square(row, col)]
    if available_moves:
        move = available_moves[np.random.randint(len(available_moves))]
        mark_square(move[0], move[1], 2)

def restart():
    screen.fill(BG_COLOR)
    draw_lines()
    global board
    board = np.zeros((BOARD_ROWS, BOARD_COLS))

player = 1  # Player 1 is human
game_over = False

draw_lines()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
            mouseX = event.pos[0]  # X coordinate
            mouseY = event.pos[1]  # Y coordinate

            clicked_row = mouseY // SQUARE_SIZE
            clicked_col = mouseX // SQUARE_SIZE

            if available_square(clicked_row, clicked_col):
                mark_square(clicked_row, clicked_col, player)
                if check_win(player):
                    display_message("Player Wins!")
                    game_over = True
                player = 2

        if player == 2 and not game_over:
            if difficulty == "easy":
                easy_ai_move()
            else:
                ai_move()
                
            if check_win(2):
                display_message("AI Wins!")
                game_over = True
            player = 1

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                restart()
                game_over = False
                player = 1

        if game_over and is_board_full():
            display_message("It's a Draw!")
            game_over = True

    draw_figures()
    pygame.display.update()
