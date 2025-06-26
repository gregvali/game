# player.py
"""Player class with hand management"""

from card import Card
from constants import PLAYER_POSITIONS_X, SCREEN_HEIGHT, CARD_DIMENSIONS, NUM_PLAYER_CARDS, PLAYER_Y_OFFSET, PLAYER_NAME

class Player:
    def __init__(self, asset_manager, name=PLAYER_NAME):
        self.asset_manager = asset_manager
        self.name = name
        self.hand = []
        self.create_hand()
    
    def create_hand(self):
        """Create player's hand with 2 joker cards"""
        y_position = SCREEN_HEIGHT - PLAYER_Y_OFFSET - CARD_DIMENSIONS[1]
        
        for i in range(NUM_PLAYER_CARDS):
            x_position = PLAYER_POSITIONS_X[i]
            card = Card(x_position, y_position, self.asset_manager, 'random')
            self.hand.append(card)
    
    def draw(self, screen):
        """Draw player's hand to the screen"""
        for card in self.hand:
            card.draw(screen)
    
    def get_card(self, index):
        """Get a card from player's hand by index"""
        if 0 <= index < len(self.hand):
            return self.hand[index]
        return None
    
    def set_card_type(self, index, card_type):
        """Set the type of a specific card in hand"""
        if 0 <= index < len(self.hand):
            self.hand[index].set_type(card_type)
    
    def get_name(self):
        """Get player's name"""
        return self.name