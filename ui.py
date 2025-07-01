# ui.py
"""UI rendering and display"""

import pygame
from constants import SCREEN_HEIGHT, NAME_Y_OFFSET, PLAYER_POSITIONS_X, NUM_PLAYERS

class UI:
    def __init__(self):
        self.font = pygame.font.Font(None, 36)
        self.small_font = pygame.font.Font(None, 24)
    
    def draw_debug_info(self, screen, ticks, input_timeout, poker_stage=0):
        """Draw debug information to screen"""
        ticks_text = self.font.render(f"Ticks: {ticks}", True, (255, 255, 255))
        timeout_text = self.font.render(f"Timeout: {input_timeout}", True, (255, 255, 255))
        stage_text = self.font.render(f"Poker Stage: {poker_stage}/3", True, (255, 255, 255))
        
        screen.blit(ticks_text, (10, 10))
        screen.blit(timeout_text, (10, 35))
        screen.blit(stage_text, (10, 60))
    
    def draw_instructions(self, screen):
        """Draw game instructions"""
        instruction_text = self.small_font.render("RIGHT: Next poker stage | LEFT: Previous stage", True, (255, 255, 255))
        stage_info = self.small_font.render("Stage 1: Cards 1-3 | Stage 2: Card 4 | Stage 3: Card 5", True, (200, 200, 200))
        hand_controls = self.small_font.render("H: Toggle hand evaluations | W: Show winners (after stage 3)", True, (200, 200, 200))
        screen.blit(instruction_text, (10, 100))
        screen.blit(stage_info, (10, 120))
        screen.blit(hand_controls, (10, 140))

    def draw_player_names(self, screen, player_names):
        """Draw player name at the bottom of screen"""
        for i in range(NUM_PLAYERS):
            name_text = self.font.render(player_names[i], True, (255, 255, 255))
            text_rect = name_text.get_rect()
            text_rect.centerx = PLAYER_POSITIONS_X[i][0] + 102
            text_rect.y = SCREEN_HEIGHT - NAME_Y_OFFSET
            screen.blit(name_text, (text_rect.x, text_rect.y))
    
    def draw_hand_evaluations(self, screen, players, board, show_evaluations=False):
        """Draw hand evaluations for all players"""
        if not show_evaluations:
            return
            
        # Get community cards (only revealed ones)
        community_cards = [card for card in board.cards if card.get_rank() is not None]
        
        if len(community_cards) < 3:  # Need at least 3 community cards
            return
        
        # Evaluate all hands
        all_results = players.evaluate_all_hands(community_cards)
        
        # Draw hand info for each player
        for i, result in enumerate(all_results):
            if result['hand_result'] is not None:
                rank, value, best_cards, description = result['hand_result']
                
                # Position text near player cards
                x_pos = PLAYER_POSITIONS_X[i][0]
                y_pos = SCREEN_HEIGHT - NAME_Y_OFFSET + 25
                
                # Draw hand description
                hand_text = self.small_font.render(description, True, (255, 255, 0))
                screen.blit(hand_text, (x_pos, y_pos))
    
    def draw_winners(self, screen, winners):
        """Draw winner announcement"""
        if not winners:
            return
        
        if len(winners) == 1:
            winner = winners[0]
            winner_text = f"Winner: {winner['player_name']}"
            hand_desc = winner['hand_result'][3] if winner['hand_result'] else "Unknown hand"
        else:
            winner_names = [w['player_name'] for w in winners]
            winner_text = f"Tie: {', '.join(winner_names)}"
            hand_desc = winners[0]['hand_result'][3] if winners[0]['hand_result'] else "Unknown hand"
        
        # Draw winner announcement in center of screen
        winner_surface = self.font.render(winner_text, True, (0, 255, 0))
        hand_surface = self.small_font.render(hand_desc, True, (255, 255, 255))
        
        winner_rect = winner_surface.get_rect(center=(650, 30))
        hand_rect = hand_surface.get_rect(center=(650, 70))
        
        screen.blit(winner_surface, winner_rect)
        screen.blit(hand_surface, hand_rect)
    
    def draw_hand_info_toggle(self, screen):
        """Draw instructions for toggling hand info"""
        toggle_text = self.small_font.render("Press H to toggle hand evaluations", True, (200, 200, 200))
        screen.blit(toggle_text, (10, 210))