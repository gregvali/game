# ui.py
"""UI rendering and display"""

import pygame

class UI:
    def __init__(self):
        self.font = pygame.font.Font(None, 36)
    
    def draw_debug_info(self, screen, ticks, input_timeout):
        """Draw debug information to screen"""
        ticks_text = self.font.render(f"Ticks: {ticks}", True, (255, 255, 255))
        timeout_text = self.font.render(f"Timeout: {input_timeout}", True, (255, 255, 255))
        
        screen.blit(ticks_text, (10, 10))
        screen.blit(timeout_text, (10, 50))
    
    def draw_instructions(self, screen):
        """Draw game instructions"""
        instruction_text = self.font.render("Press RIGHT arrow to play cards", True, (255, 255, 255))
        screen.blit(instruction_text, (10, 90))