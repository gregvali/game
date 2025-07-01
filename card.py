# card.py
"""Card class and related functionality"""

import pygame
from constants import CARD_DIMENSIONS

class Card:
    def __init__(self, x, y, asset_manager, card_type='base'):
        self.x = x
        self.y = y
        self.asset_manager = asset_manager
        self.set_type(card_type)
        self.rect = pygame.Rect(x, y, CARD_DIMENSIONS[0], CARD_DIMENSIONS[1])
    
    def set_type(self, card_type):
        """Change the card type"""
        if card_type == 'random':
            self.card_type = self.asset_manager.get_random_asset_key()
        else:
            self.card_type = card_type

    def get_type(self):
        return self.card_type

    def get_asset(self):
        """Get the current asset for this card"""
        return self.asset_manager.get_asset(self.card_type)
    
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

    def get_rank(self):
        """Get the rank of the card (2-14, where 11=J, 12=Q, 13=K, 14=A)"""
        if self.card_type == 'base' or self.card_type == 'joker':
            return None
            
        rank_char = self.card_type[0].lower()
        if rank_char == 'a':
            return 14
        elif rank_char == 'k':
            return 13
        elif rank_char == 'q':
            return 12
        elif rank_char == 'j':
            return 11
        elif rank_char == 't':
            return 10
        else:
            return int(rank_char)
    
    def get_suit(self):
        """Get the suit of the card (hearts, diamonds, clubs, spades)"""
        if self.card_type == 'base' or self.card_type == 'joker':
            return None
            
        suit_char = self.card_type[1].lower()
        suit_map = {'h': 'hearts', 'd': 'diamonds', 'c': 'clubs', 's': 'spades'}
        return suit_map.get(suit_char)
    
    def get_rank_name(self):
        """Get human-readable rank name"""
        rank = self.get_rank()
        if rank is None:
            return None
        rank_names = {11: 'Jack', 12: 'Queen', 13: 'King', 14: 'Ace'}
        return rank_names.get(rank, str(rank))
    
    def __str__(self):
        """String representation of the card"""
        if self.card_type in ['base', 'joker']:
            return self.card_type
        return f"{self.get_rank_name()} of {self.get_suit().title()}"