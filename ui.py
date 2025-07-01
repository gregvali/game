# ui.py
"""UI rendering and display"""

import pygame
from constants import SCREEN_HEIGHT, NAME_Y_OFFSET, PLAYER_POSITIONS_X, NUM_PLAYERS

class UI:
    def __init__(self):
        self.font = pygame.font.Font(None, 36)
    
    def draw_debug_info(self, screen, ticks, input_timeout, poker_stage=0):
        """Draw debug information to screen"""
        ticks_text = self.font.render(f"Ticks: {ticks}", True, (255, 255, 255))
        timeout_text = self.font.render(f"Timeout: {input_timeout}", True, (255, 255, 255))
        stage_text = self.font.render(f"Poker Stage: {poker_stage}/3", True, (255, 255, 255))
        
        screen.blit(ticks_text, (10, 10))
        screen.blit(timeout_text, (10, 50))
        screen.blit(stage_text, (10, 90))
    
    def draw_instructions(self, screen):
        """Draw game instructions"""
        instruction_text = self.font.render("RIGHT: Next poker stage | LEFT: Previous stage", True, (255, 255, 255))
        stage_info = self.font.render("Stage 1: Cards 1-3 | Stage 2: Card 4 | Stage 3: Card 5", True, (200, 200, 200))
        screen.blit(instruction_text, (10, 130))
        screen.blit(stage_info, (10, 170))

    def draw_player_names(self, screen, player_names):
        """Draw player name at the bottom of screen"""
        for i in range(NUM_PLAYERS):
            name_text = self.font.render(player_names[i], True, (255, 255, 255))
            text_rect = name_text.get_rect()
            text_rect.centerx = PLAYER_POSITIONS_X[i][0] + 102
            text_rect.y = SCREEN_HEIGHT - NAME_Y_OFFSET
            screen.blit(name_text, (text_rect.x, text_rect.y))