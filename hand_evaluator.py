# hand_evaluator.py
"""Poker hand evaluation system"""

from collections import Counter
from enum import Enum

class HandRank(Enum):
    """Poker hand rankings (higher value = better hand)"""
    HIGH_CARD = 1
    PAIR = 2
    TWO_PAIR = 3
    THREE_OF_A_KIND = 4
    STRAIGHT = 5
    FLUSH = 6
    FULL_HOUSE = 7
    FOUR_OF_A_KIND = 8
    STRAIGHT_FLUSH = 9
    ROYAL_FLUSH = 10

class HandEvaluator:
    def __init__(self):
        pass
    
    def evaluate_hand(self, player_cards, community_cards):
        """
        Evaluate the best 5-card hand from 7 available cards
        Returns: (HandRank, hand_value, best_cards, description)
        """
        # Filter out base/joker cards and get only real cards
        all_cards = []
        for card in player_cards + community_cards:
            if card.get_rank() is not None and card.get_suit() is not None:
                all_cards.append(card)
        
        if len(all_cards) < 5:
            return None  # Not enough cards to evaluate
        
        # Generate all possible 5-card combinations
        from itertools import combinations
        best_hand = None
        best_rank = HandRank.HIGH_CARD
        best_value = 0
        best_cards = []
        
        for five_cards in combinations(all_cards, 5):
            rank, value, description = self._evaluate_five_cards(list(five_cards))
            if self._is_better_hand(rank, value, best_rank, best_value):
                best_hand = description
                best_rank = rank
                best_value = value
                best_cards = list(five_cards)
        
        return best_rank, best_value, best_cards, best_hand
    
    def _evaluate_five_cards(self, cards):
        """Evaluate exactly 5 cards and return rank, value, and description"""
        ranks = sorted([card.get_rank() for card in cards], reverse=True)
        suits = [card.get_suit() for card in cards]
        
        # Check for flush
        is_flush = len(set(suits)) == 1
        
        # Check for straight
        is_straight = self._is_straight(ranks)
        
        # Special case: A-2-3-4-5 straight (wheel)
        if ranks == [14, 5, 4, 3, 2]:
            is_straight = True
            ranks = [5, 4, 3, 2, 1]  # Ace low
        
        # Count rank frequencies
        rank_counts = Counter(ranks)
        counts = sorted(rank_counts.values(), reverse=True)
        unique_ranks = sorted(rank_counts.keys(), key=lambda x: (rank_counts[x], x), reverse=True)
        
        # Determine hand type
        if is_straight and is_flush:
            if ranks[0] == 14 and ranks[1] == 13:  # Royal flush
                return HandRank.ROYAL_FLUSH, ranks[0], "Royal Flush"
            else:
                return HandRank.STRAIGHT_FLUSH, ranks[0], f"Straight Flush, {self._rank_name(ranks[0])} high"
        
        elif counts == [4, 1]:  # Four of a kind
            quad_rank = unique_ranks[0]
            kicker = unique_ranks[1]
            return HandRank.FOUR_OF_A_KIND, (quad_rank, kicker), f"Four {self._rank_name(quad_rank)}s"
        
        elif counts == [3, 2]:  # Full house
            trips_rank = unique_ranks[0]
            pair_rank = unique_ranks[1]
            return HandRank.FULL_HOUSE, (trips_rank, pair_rank), f"Full House, {self._rank_name(trips_rank)}s over {self._rank_name(pair_rank)}s"
        
        elif is_flush:
            return HandRank.FLUSH, tuple(ranks), f"Flush, {self._rank_name(ranks[0])} high"
        
        elif is_straight:
            return HandRank.STRAIGHT, ranks[0], f"Straight, {self._rank_name(ranks[0])} high"
        
        elif counts == [3, 1, 1]:  # Three of a kind
            trips_rank = unique_ranks[0]
            kickers = sorted([r for r in ranks if r != trips_rank], reverse=True)
            return HandRank.THREE_OF_A_KIND, (trips_rank, tuple(kickers)), f"Three {self._rank_name(trips_rank)}s"
        
        elif counts == [2, 2, 1]:  # Two pair
            pairs = sorted([r for r, c in rank_counts.items() if c == 2], reverse=True)
            kicker = [r for r, c in rank_counts.items() if c == 1][0]
            return HandRank.TWO_PAIR, (tuple(pairs), kicker), f"Two Pair, {self._rank_name(pairs[0])}s and {self._rank_name(pairs[1])}s"
        
        elif counts == [2, 1, 1, 1]:  # One pair
            pair_rank = [r for r, c in rank_counts.items() if c == 2][0]
            kickers = sorted([r for r in ranks if r != pair_rank], reverse=True)
            return HandRank.PAIR, (pair_rank, tuple(kickers)), f"Pair of {self._rank_name(pair_rank)}s"
        
        else:  # High card
            return HandRank.HIGH_CARD, tuple(ranks), f"High Card, {self._rank_name(ranks[0])}"
    
    def _is_straight(self, ranks):
        """Check if ranks form a straight"""
        if len(set(ranks)) != 5:
            return False
        return ranks[0] - ranks[4] == 4
    
    def _rank_name(self, rank):
        """Convert rank number to name"""
        names = {11: 'Jack', 12: 'Queen', 13: 'King', 14: 'Ace'}
        return names.get(rank, str(rank))
    
    def compare_hands(self, hand1_result, hand2_result):
        """
        Compare two hand evaluation results
        Returns: 1 if hand1 wins, -1 if hand2 wins, 0 if tie
        """
        if hand1_result is None and hand2_result is None:
            return 0
        if hand1_result is None:
            return -1
        if hand2_result is None:
            return 1
        
        rank1, value1, _, _ = hand1_result
        rank2, value2, _, _ = hand2_result
        
        if rank1.value > rank2.value:
            return 1
        elif rank1.value < rank2.value:
            return -1
        else:
            # Same rank, compare values using our helper method
            return self._compare_values(value1, value2)
    
    def _is_better_hand(self, rank1, value1, rank2, value2):
        """Compare two hands to see if the first is better"""
        # First compare hand ranks
        if rank1.value > rank2.value:
            return True
        elif rank1.value < rank2.value:
            return False
        
        # Same rank, compare values (need to handle different value types)
        return self._compare_values(value1, value2) > 0
    
    def _compare_values(self, value1, value2):
        """
        Compare hand values, handling different types (int, tuple)
        Returns: 1 if value1 > value2, -1 if value1 < value2, 0 if equal
        """
        # Convert single values to tuples for consistent comparison
        if not isinstance(value1, tuple):
            value1 = (value1,)
        if not isinstance(value2, tuple):
            value2 = (value2,)
        
        # Compare element by element
        for v1, v2 in zip(value1, value2):
            if isinstance(v1, tuple) and isinstance(v2, tuple):
                # Recursively compare nested tuples
                result = self._compare_values(v1, v2)
                if result != 0:
                    return result
            else:
                if v1 > v2:
                    return 1
                elif v1 < v2:
                    return -1
        
        # If we get here, they're equal
        return 0
