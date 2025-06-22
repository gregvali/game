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
    'base': "assets/base_card.png",
    "as": "assets/AS.png",
    "2s": "assets/2S.png",
    "3s": "assets/3S.png",
    "4s": "assets/4S.png",
    "5s": "assets/5S.png",
    "6s": "assets/6S.png",
    "7s": "assets/7S.png",
    "8s": "assets/8S.png",
    "9s": "assets/9S.png",
    "ts": "assets/TS.png",
    "js": "assets/JS.png",
    "qs": "assets/QS.png",
    "ks": "assets/KS.png",
    "ac": "assets/ac.png",
    "2c": "assets/2c.png",
    "3c": "assets/3c.png",
    "4c": "assets/4c.png",
    "5c": "assets/5c.png",
    "6c": "assets/6c.png",
    "7c": "assets/7c.png",
    "8c": "assets/8c.png",
    "9c": "assets/9c.png",
    "tc": "assets/tc.png",
    "jc": "assets/jc.png",
    "qc": "assets/qc.png",
    "kc": "assets/kc.png",
    "ad": "assets/Ad.png",
    "2d": "assets/2d.png",
    "3d": "assets/3d.png",
    "4d": "assets/4d.png",
    "5d": "assets/5d.png",
    "6d": "assets/6d.png",
    "7d": "assets/7d.png",
    "8d": "assets/8d.png",
    "9d": "assets/9d.png",
    "td": "assets/Td.png",
    "jd": "assets/Jd.png",
    "qd": "assets/Qd.png",
    "kd": "assets/Kd.png",
    "ah": "assets/ah.png",
    "2h": "assets/2h.png",
    "3h": "assets/3h.png",
    "4h": "assets/4h.png",
    "5h": "assets/5h.png",
    "6h": "assets/6h.png",
    "7h": "assets/7h.png",
    "8h": "assets/8h.png",
    "9h": "assets/9h.png",
    "th": "assets/th.png",
    "jh": "assets/jh.png",
    "qh": "assets/qh.png",
    "kh": "assets/kh.png"
}