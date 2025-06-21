# input_handler.py
"""Input handling and management"""

import pygame
from constants import INPUT_DELAY_IN_TICKS, NUM_BOARD_CARDS

class InputHandler:
    def __init__(self):
        self.input_timeout = 0
        self.poker_stage = 0  # 0: not started, 1: first 3 cards, 2: fourth card, 3: fifth card
    
    def update(self):
        """Update input timeout"""
        if self.input_timeout != 0:
            self.input_timeout += 1
            if self.input_timeout >= INPUT_DELAY_IN_TICKS:
                self.input_timeout = 0
    
    def handle_input(self, board):
        """Handle keyboard input - poker style card opening"""
        keys = pygame.key.get_pressed()
        
        if self.input_timeout == 0:
            if keys[pygame.K_RIGHT] and self.poker_stage < 3:
                self.poker_stage += 1
                
                if self.poker_stage == 1:
                    # First press: open cards 0, 1, 2 (first three cards)
                    board.set_card_type(0, 'joker')
                    board.set_card_type(1, 'joker') 
                    board.set_card_type(2, 'joker')
                elif self.poker_stage == 2:
                    # Second press: open card 3 (fourth card)
                    board.set_card_type(3, 'joker')
                elif self.poker_stage == 3:
                    # Third press: open card 4 (fifth card)
                    board.set_card_type(4, 'joker')
                
                self.input_timeout = 1
            elif keys[pygame.K_LEFT] and self.poker_stage > 0:
                # Optional: Allow going back one stage
                if self.poker_stage == 3:
                    board.set_card_type(4, 'base')
                elif self.poker_stage == 2:
                    board.set_card_type(3, 'base')
                elif self.poker_stage == 1:
                    board.set_card_type(0, 'base')
                    board.set_card_type(1, 'base')
                    board.set_card_type(2, 'base')
                
                self.poker_stage -= 1
                self.input_timeout = 1
    
    def get_timeout(self):
        """Get current input timeout"""
        return self.input_timeout
    
    def get_poker_stage(self):
        """Get current poker stage"""
        return self.poker_stage