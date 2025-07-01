# player.py
"""Player class with hand management"""

from card import Card
from constants import PLAYER_POSITIONS_X, SCREEN_HEIGHT, CARD_DIMENSIONS, NUM_PLAYER_CARDS, PLAYER_Y_OFFSET, NUM_PLAYERS, PLAYER_NAMES

class Players:
    def __init__(self, asset_manager, names=PLAYER_NAMES):
        self.asset_manager = asset_manager
        self.names = names
        self.in_play = []
        self.create_hands()
    
    def create_hands(self):
        y_position = SCREEN_HEIGHT - PLAYER_Y_OFFSET - CARD_DIMENSIONS[1]
        
        for i in range(NUM_PLAYERS):
            for j in range(NUM_PLAYER_CARDS):
                x_position = PLAYER_POSITIONS_X[i][j]
                card = Card(x_position, y_position, self.asset_manager, 'random')
                self.in_play.append(card)
    
    def draw(self, screen):
        for card in self.in_play:
            card.draw(screen)
    
    def get_card(self, index):
        if 0 <= index < len(self.in_play):
            return self.in_play[index]
        return None
    
    def set_card_type(self, index, card_type):
        if 0 <= index < len(self.in_play):
            self.in_play[index].set_type(card_type)
    
    def get_names(self):
        """Get players' names"""
        return self.names