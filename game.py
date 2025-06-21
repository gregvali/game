# game.py
"""Main game class"""

import pygame
import sys
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, FPS, BG_COLOR
from asset_manager import AssetManager
from board import Board
from player import Player
from input_handler import InputHandler
from ui import UI

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Simple Game MVP - Refactored")
        self.clock = pygame.time.Clock()
        
        # Initialize game components
        self.asset_manager = AssetManager()
        self.board = Board(self.asset_manager)
        self.player = Player(self.asset_manager)
        self.input_handler = InputHandler()
        self.ui = UI()
        
        # Game state
        self.ticks = 0
        self.running = True
    
    def handle_events(self):
        """Handle pygame events"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.running = False
    
    def update(self):
        """Update game state"""
        self.input_handler.handle_input(self.board)
        self.input_handler.update()
        self.ticks += 1
    
    def render(self):
        """Render the game"""
        self.screen.fill(BG_COLOR)
        
        # Draw game objects
        self.board.draw(self.screen)
        self.player.draw(self.screen)
        
        # Draw UI
        self.ui.draw_debug_info(self.screen, self.ticks, self.input_handler.get_timeout(), self.input_handler.get_poker_stage())
        self.ui.draw_instructions(self.screen)
        self.ui.draw_player_name(self.screen, self.player.get_name())
        
        pygame.display.flip()
    
    def run(self):
        """Main game loop"""
        while self.running:
            self.handle_events()
            self.update()
            self.render()
            self.clock.tick(FPS)
        
        self.quit()
    
    def quit(self):
        """Clean up and exit"""
        pygame.quit()
        sys.exit()