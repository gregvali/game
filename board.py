# board.py
"""Game board and card management"""

from card import Card
from constants import CARD_POSITIONS_X, SCREEN_HEIGHT, PLAYER_HEIGHT, CARD_DIMENSIONS, NUM_CARDS

class Board:
    def __init__(self, asset_manager):
        self.asset_manager = asset_manager
        self.cards = []
        self.create_cards()
    
    def create_cards(self):
        """Create all cards in their initial positions"""
        y_position = SCREEN_HEIGHT - PLAYER_HEIGHT - CARD_DIMENSIONS[1]
        
        for i in range(NUM_CARDS):
            x_position = CARD_POSITIONS_X[i]
            card = Card(x_position, y_position, self.asset_manager, 'base')
            self.cards.append(card)
    
    def set_card_type(self, index, card_type):
        """Set the type of a specific card"""
        if 0 <= index < len(self.cards):
            self.cards[index].set_type(card_type)
    
    def draw(self, screen):
        """Draw all cards to the screen"""
        for card in self.cards:
            card.draw(screen)
    
    def get_card(self, index):
        """Get a card by index"""
        if 0 <= index < len(self.cards):
            return self.cards[index]
        return None