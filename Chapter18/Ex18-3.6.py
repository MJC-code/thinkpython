"""This module contains a code example related to

Think Python, 2nd Edition
by Allen Downey
http://thinkpython2.com

Copyright 2015 Allen Downey

License: http://creativecommons.org/licenses/by/4.0/
"""

from __future__ import print_function, division

from Card import Hand, Deck
from heapq import nlargest

class PokerHand(Hand):
    """Represents a poker hand."""

    def suit_and_rank_hist(self):
        """Builds histograms of the suits and ranks that appear in the hand.
        Stores the result in attributes suits and ranks.
        """
        self.suits = {}
        self.ranks = {}
        
        for card in self.cards:
            self.suits[card.suit] = self.suits.get(card.suit, 0) + 1
            self.ranks[card.rank] = self.ranks.get(card.rank, 0) + 1

        
    def has_pair(self):
        """Tests whether a PokerHand contains 2 of the same rank"""
        self.suit_and_rank_hist()
        for val in self.ranks.values():
            if val >= 2:
                return True
        return False

    def has_twopair(self):
        """Tests whether a PokerHand contains 2 pairs of same rank"""
        self.suit_and_rank_hist()
        pairs = 0
        for val in self.ranks.values():
            if val >= 2:
                pairs += 1
        return pairs >=2

    def has_threekind(self):
        """"Tests PokerHand for 3 of same rank"""
        self.suit_and_rank_hist()
        for val in self.ranks.values():
            if val >= 3:
                return True
        return False

    def has_straight(self):
        """Tests PokerHand for 5 cards with ranks in sequence"""
        self.suit_and_rank_hist()
        ranks = self.ranks.copy()
        ranks[14] = ranks.get(1, 0) # Makes Aces high as well as low
        counter = 0
        for i in range(1, 14):
            if ranks.get(i, 0) >= 1:
                counter += 1
                if counter >= 5:
                    return True
            else:
                counter = 0
        return False

    def has_flush(self):
        """Returns True if the hand has a flush (5 cards with same suit), False otherwise.
        Note that this works correctly for hands with more than 5 cards.
        """
        self.suit_and_rank_hist()
        for val in self.suits.values():
            if val >= 5:
                return True
        return False

    def has_fullhouse(self):
        """Tests PokerHand for 3 of one rank, two of another"""
        self.suit_and_rank_hist()
        two_most_common_cards = nlargest(2, self.ranks, key=self.ranks.get)
        if self.ranks.get(two_most_common_cards[0]) >= 3:
            if self.ranks.get(two_most_common_cards[1]) >= 2:
                return True
        return False
        
    def has_fourkind(self):
        """Tests a PokerHand for 4 of same rank"""
        self.suit_and_rank_hist()
        for val in self.ranks.values():
            if val >= 4:
                return True
        return False

    def has_straightflush(self):
        """Tests a PokerHand for 5 cards of same suit with ranks in a sequence"""
        self.suit_and_rank_hist()

        d = {} # Build a dictionary of PokerHands. Key = suit, val = PokerHand of cards of that suit in self.cards
        for card in self.cards:
            d.setdefault(card.suit, PokerHand()).add_card(card)
        for hand in d.values():
            if len(hand.cards) >= 5:
                hand.suit_and_rank_hist()
                if hand.has_straight():
                    return True
        return False

    def classify(self):
        """Works out the highest-value classification for a PokerHand
        Assigns that classification to self.label
        """
        if self.has_straightflush():
            label = 'Straight flush'
        elif self.has_fourkind():
            label = 'Four of a kind'
        elif self.has_fullhouse():
            label = 'Full house'
        elif self.has_flush():
            label = 'Flush'
        elif self.has_straight():
            label = 'Straight'
        elif self.has_threekind():
            label = 'Three of a kind'
        elif self.has_twopair():
            label = 'Two pairs'
        elif self.has_pair():
            label = 'Pair'
        else:
            label = 'Nothing'
        self.label = label
                
        
def count(deck, num_hands, num_cards):
    """Shuffles deck, draws num_hands hands of size num_cards.
    Classifies each hand, and adds the result to the global dictionary results
    """
    global result
    for i in range(num_hands):
        deck.shuffle()
        hand = PokerHand()
        deck.move_cards(hand, num_cards)
        hand.sort()
#        print(hand)
        hand.classify()
        if hand.label not in result:
            result[hand.label] = 1
        else:
            result[hand.label] += 1
    
        
if __name__ == '__main__':
    # Result is a globabl dictionary of hand classifcations --> frequencies
    deals = 20000 #number of deals to make
    num_hands = 4 #hands per deal
    num_cards = 5 # cards per hand
    result = dict()
    
    for i in range(deals):
        deck = Deck()
        count(deck, num_hands, num_cards)

    hands = deals * num_hands
    print('For', num_cards, 'card hands, the frequencies are:\n')
    for score in result:
        print(score, 'occurs in', "{:.3f}".format(result[score]/hands*100),
    '% of the hands') 
    
      
