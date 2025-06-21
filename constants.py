# constants.py
"""Game constants and configuration"""

# Screen settings
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60
BG_COLOR = (30, 30, 30)

# Player settings
PLAYER_HEIGHT = 40
PLAYER_SPEED = 5
PLAYER_NAME = "Player 1"

# Card settings
CARD_DIMENSIONS = (100, 140)
BOARD_POSITIONS_X = (130, 240, 350, 460, 570)
PLAYER_POSITIONS_X = (300, 420)  # Two cards centered
NUM_BOARD_CARDS = 5
NUM_PLAYER_CARDS = 2

# Layout settings
BOARD_Y_OFFSET = 200  # Distance from top for board cards
PLAYER_Y_OFFSET = 80  # Distance from bottom for player cards
NAME_Y_OFFSET = 60    # Distance from bottom for player name

# Input settings
INPUT_DELAY_IN_TICKS = 10

# Asset paths
ASSETS = {
    'joker': "assets/balatro_joker.png",
    'ace': "assets/standard_ace.png", 
    'base': "assets/base_card.png"
}