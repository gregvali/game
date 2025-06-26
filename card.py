# card.py
"""Card class and related functionality"""

import random
import pygame
from constants import CARD_DIMENSIONS, ASSETS

class Card:
    def __init__(self, x, y, asset_manager, card_type='base'):
        self.x = x
        self.y = y
        self.asset_manager = asset_manager
        self.card_type = card_type
        self.rect = pygame.Rect(x, y, CARD_DIMENSIONS[0], CARD_DIMENSIONS[1])
    
    def set_type(self, card_type):
        """Change the card type"""
        self.card_type = card_type
    
    def set_random_type(self):
        self.card_type = self.get_random_card()
        print(self.card_type)

    def get_asset(self):
        """Get the current asset for this card"""
        return self.asset_manager.get_asset(self.card_type)
    
    def get_random_card(self):
        random_id = random.randint(2, 53)
        keys = list(ASSETS.keys())
        return keys[random_id]
    
    def draw(self, screen):
        """Draw the card to the screen"""
        asset = self.get_asset()
        screen.blit(asset, (self.x, self.y))
    
    def update_position(self, x, y):
        """Update card position"""
        self.x = x
        self.y = y
        self.rect.x = x
        self.rect.y = y