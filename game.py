import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60
BG_COLOR = (30, 30, 30)
PLAYER_HEIGHT = 40
CARD_DIMENSIONS = (100, 140)
CARD_POSITIONS_X = (130, 240, 350, 460, 570)
INPUT_DELAY_IN_TICKS = 20

# Initialize screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Simple Game MVP")
clock = pygame.time.Clock()

# Game state
player_speed = 5
ticks = 0
selected_card = 0
input_timeout = 0
running = True

# PLAYER
def render_asset(asset_dest):
    card_asset = pygame.image.load(asset_dest)
    print(card_asset.get_width())
    card_asset = pygame.transform.scale(card_asset, (CARD_DIMENSIONS[0], CARD_DIMENSIONS[1]))
    return card_asset

joker_asset = render_asset("assets/balatro_joker.png")
ace_asset = render_asset("assets/standard_ace.png")
base_asset = render_asset("assets/base_card.png")

card_pos = [
[ CARD_POSITIONS_X[0], SCREEN_HEIGHT - PLAYER_HEIGHT - CARD_DIMENSIONS[1] ],
[ CARD_POSITIONS_X[1], SCREEN_HEIGHT - PLAYER_HEIGHT - CARD_DIMENSIONS[1] ],
[ CARD_POSITIONS_X[2], SCREEN_HEIGHT - PLAYER_HEIGHT - CARD_DIMENSIONS[1] ],
[ CARD_POSITIONS_X[3], SCREEN_HEIGHT - PLAYER_HEIGHT - CARD_DIMENSIONS[1] ],
[ CARD_POSITIONS_X[4], SCREEN_HEIGHT - PLAYER_HEIGHT - CARD_DIMENSIONS[1] ]
            ]

board = [
    base_asset,
    base_asset,
    base_asset,
    base_asset,
    base_asset
]
    
def draw_card(asset, position):
    screen.blit(asset, position)

def render_players(board, positions):
    i = 0
    for pos in positions:
        draw_card(board[i], pos)
        i += 1

def handle_input():
    global selected_card
    global input_timeout
    keys = pygame.key.get_pressed()

    if input_timeout == 0:
        if keys[pygame.K_RIGHT] and selected_card < 5: 
            board[selected_card] = joker_asset
            selected_card += 1
            input_timeout += 1
    
def update_game():
    global ticks
    global input_timeout
    # Placeholder for game logic
    ticks += 1  # Increment score as a simple timer
    if input_timeout != 0:
        input_timeout += 1
    if input_timeout == INPUT_DELAY_IN_TICKS:
        input_timeout = 0

def render():
    screen.fill(BG_COLOR)
    render_players(board, card_pos)
    draw_ticks()
    pygame.display.flip()

def draw_ticks():
    font = pygame.font.Font(None, 36)
    ticks_text = font.render(f"ticks: {ticks}", True, (255, 255, 255))
    input_timeout_text = font.render(f"Timeout: {input_timeout}", True, (255, 255, 255))
    screen.blit(ticks_text, (10, 10))
    screen.blit(input_timeout_text, (10, 40))

# Main game loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    handle_input()
    update_game()
    render()

    clock.tick(FPS)

pygame.quit()
sys.exit()