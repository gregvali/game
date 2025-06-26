# board.py
"""Game board and card management"""

from card import Card
from constants import BOARD_POSITIONS_X, SCREEN_HEIGHT, CARD_DIMENSIONS, NUM_BOARD_CARDS, BOARD_Y_OFFSET

class Board:
    def __init__(self, asset_manager):
        self.asset_manager = asset_manager
        self.cards = []
        self.create_cards()
    
    def create_cards(self):
        """Create all cards in their initial positions"""
        y_position = BOARD_Y_OFFSET
        
        for i in range(NUM_BOARD_CARDS):
            x_position = BOARD_POSITIONS_X[i]
            card = Card(x_position, y_position, self.asset_manager, 'base')
            self.cards.append(card)
    
    def set_card_type(self, index, card_type):
        """Set the type of a specific card"""
        if 0 <= index < len(self.cards):
            if card_type == 'random':
                self.cards[index].set_random_type()
            else:
                self.cards[index].set_type(card_type)
    
    def next_card(self, stage, card_type):
        if stage == 1:
            # First press: open cards 0, 1, 2 (first three cards)
            for i in range(3):
                self.set_card_type(i, card_type)
        elif stage == 2:
            # Second press: open card 3 (fourth card)
            self.set_card_type(3, card_type)
        elif stage == 3:
            # Third press: open card 4 (fifth card)
            self.set_card_type(4, card_type)

    def reset_board(self):
        for card in self.cards:
            card.card_type = 'base'
        
    def draw(self, screen):
        """Draw all cards to the screen"""
        for card in self.cards:
            card.draw(screen)
    
    def get_card(self, index):
        """Get a card by index"""
        if 0 <= index < len(self.cards):
            return self.cards[index]
        return None