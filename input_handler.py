# input_handler.py
"""Input handling and management"""

import pygame
from constants import INPUT_DELAY_IN_TICKS, NUM_BOARD_CARDS

RANDOM = 'random'
class InputHandler:
    def __init__(self):
        self.input_timeout = 0
        self.poker_stage = 0  # 0: not started, 1: first 3 cards, 2: fourth card, 3: fifth card
        self.show_hand_evaluations = False
        self.show_winners = False
    
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
            if keys[pygame.K_RIGHT]:
                self.handle_key_right(board)
            elif keys[pygame.K_LEFT]:
                self.handle_key_left(board)
            elif keys[pygame.K_h]:
                self.toggle_hand_evaluations()
            elif keys[pygame.K_w]:
                self.toggle_winners()
    
    def handle_key_right(self, board):
        if self.poker_stage < 3:
            self.poker_stage += 1
            board.next_card(self.poker_stage, RANDOM)
            self.input_timeout = 1

    def handle_key_left(self, board):
        if self.poker_stage > 0:
            board.reset_board()
            self.poker_stage = 0
            self.input_timeout = 1

    def toggle_hand_evaluations(self):
        """Toggle display of hand evaluations"""
        self.show_hand_evaluations = not self.show_hand_evaluations
        self.input_timeout = 1
    
    def toggle_winners(self):
        """Toggle display of winners"""
        self.show_winners = not self.show_winners
        self.input_timeout = 1
    
    def get_timeout(self):
        """Get current input timeout"""
        return self.input_timeout
    
    def get_poker_stage(self):
        """Get current poker stage"""
        return self.poker_stage
    
    def get_show_hand_evaluations(self):
        """Get whether to show hand evaluations"""
        return self.show_hand_evaluations
    
    def get_show_winners(self):
        """Get whether to show winners"""
        return self.show_winners