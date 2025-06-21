# input_handler.py
"""Input handling and management"""

import pygame
from constants import INPUT_DELAY_IN_TICKS, NUM_CARDS

class InputHandler:
    def __init__(self):
        self.input_timeout = 0
        self.selected_card = 0
    
    def update(self):
        """Update input timeout"""
        if self.input_timeout != 0:
            self.input_timeout += 1
            if self.input_timeout >= INPUT_DELAY_IN_TICKS:
                self.input_timeout = 0
    
    def handle_input(self, board):
        """Handle keyboard input"""
        keys = pygame.key.get_pressed()
        
        if self.input_timeout == 0:
            if keys[pygame.K_RIGHT] and self.selected_card < NUM_CARDS:
                board.set_card_type(self.selected_card, 'joker')
                self.selected_card += 1
                self.input_timeout = 1
            elif keys[pygame.K_LEFT] and self.selected_card > 0:
                self.selected_card -= 1
                board.set_card_type(self.selected_card, 'ace')
                self.input_timeout = 1
    
    def get_timeout(self):
        """Get current input timeout"""
        return self.input_timeout