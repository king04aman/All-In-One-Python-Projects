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

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Tic Tac Toe')
screen.fill(BG_COLOR)

board = np.zeros((BOARD_ROWS, BOARD_COLS))

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


# Minimax algorithm
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


# AI Move
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
                    game_over = True
                player = 2

        if player == 2 and not game_over:
            ai_move()
            if check_win(2):
                game_over = True
            player = 1

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                restart()
                game_over = False
                player = 1

    draw_figures()
    pygame.display.update()
