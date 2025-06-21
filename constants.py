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

# Card settings
CARD_DIMENSIONS = (100, 140)
CARD_POSITIONS_X = (130, 240, 350, 460, 570)
NUM_CARDS = 5

# Input settings
INPUT_DELAY_IN_TICKS = 15

# Asset paths
ASSETS = {
    'joker': "assets/balatro_joker.png",
    'ace': "assets/standard_ace.png", 
    'base': "assets/base_card.png"
}