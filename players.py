# player.py
"""Player class with hand management"""

from card import Card
from constants import PLAYER_POSITIONS_X, SCREEN_HEIGHT, CARD_DIMENSIONS, NUM_PLAYER_CARDS, PLAYER_Y_OFFSET, NUM_PLAYERS, PLAYER_NAMES
from hand_evaluator import HandEvaluator

class Players:
    def __init__(self, asset_manager, names=PLAYER_NAMES):
        self.asset_manager = asset_manager
        self.names = names
        self.in_play = []
        self.hand_evaluator = HandEvaluator()
        self.create_hands()
    
    def create_hands(self):
        y_position = SCREEN_HEIGHT - PLAYER_Y_OFFSET - CARD_DIMENSIONS[1]
        
        for i in range(NUM_PLAYERS):
            for j in range(NUM_PLAYER_CARDS):
                x_position = PLAYER_POSITIONS_X[i][j]
                card = Card(x_position, y_position, self.asset_manager, 'random')
                self.in_play.append(card)
    
    def draw(self, screen):
        for card in self.in_play:
            card.draw(screen)
    
    def get_card(self, index):
        if 0 <= index < len(self.in_play):
            return self.in_play[index]
        return None
    
    def set_card_type(self, index, card_type):
        if 0 <= index < len(self.in_play):
            self.in_play[index].set_type(card_type)
    
    def get_names(self):
        """Get players' names"""
        return self.names
    
    def get_player_cards(self, player_index):
        """Get the cards for a specific player"""
        if player_index < 0 or player_index >= NUM_PLAYERS:
            return []
        
        start_index = player_index * NUM_PLAYER_CARDS
        end_index = start_index + NUM_PLAYER_CARDS
        return self.in_play[start_index:end_index]
    
    def evaluate_player_hand(self, player_index, community_cards):
        """Evaluate a player's best hand using their cards + community cards"""
        player_cards = self.get_player_cards(player_index)
        return self.hand_evaluator.evaluate_hand(player_cards, community_cards)
    
    def evaluate_all_hands(self, community_cards):
        """Evaluate all players' hands and return results"""
        results = []
        for i in range(NUM_PLAYERS):
            hand_result = self.evaluate_player_hand(i, community_cards)
            results.append({
                'player_index': i,
                'player_name': self.names[i],
                'hand_result': hand_result
            })
        return results
    
    def find_winners(self, community_cards):
        """Find the winning player(s) and return detailed results"""
        all_results = self.evaluate_all_hands(community_cards)
        
        # Filter out players with no valid hand
        valid_results = [r for r in all_results if r['hand_result'] is not None]
        
        if not valid_results:
            return []
        
        # Find the best hand(s)
        best_results = [valid_results[0]]
        
        for result in valid_results[1:]:
            comparison = self.hand_evaluator.compare_hands(
                result['hand_result'], 
                best_results[0]['hand_result']
            )
            
            if comparison > 0:  # This hand is better
                best_results = [result]
            elif comparison == 0:  # Tie
                best_results.append(result)
        
        return best_results