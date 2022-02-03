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
        """Builds a histogram of the suits and ranks that appear in the hand.

        Stores the result in attributes suits and ranks.
        """
        self.suits = {}
        self.ranks = {}
        
        for card in self.cards:
            self.suits[card.suit] = self.suits.get(card.suit, 0) + 1
            self.ranks[card.rank] = self.ranks.get(card.rank, 0) + 1

        
    def has_pair(self):
        self.suit_and_rank_hist()
        for val in self.ranks.values():
            if val >= 2:
                return True
        return False

    def has_twopair(self):
        self.suit_and_rank_hist()
        pairs = 0
        for val in self.ranks.values():
            if val >= 2:
                pairs += 1
        return pairs >=2

    def three_of_kind(self):
        self.suit_and_rank_hist()
        for val in self.ranks.values():
            if val >= 3:
                return True
        return False

    def has_straight(self):
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
        """Returns True if the hand has a flush, False otherwise.
        Note that this works correctly for hands with more than 5 cards.
        """
        self.suit_and_rank_hist()
        for val in self.suits.values():
            if val >= 5:
                return True
        return False

    def has_full_house(self):
        self.suit_and_rank_hist()
        two_most_common_cards = nlargest(2, self.suits, key=self.suits.get)
        if self.suits.get(two_most_common_cards[0]) >= 3:
            if self.suits.get(two_most_common_cards[1]) >= 2:
                return True
        return False
        
    def has_four_of_kind(self):
        self.suit_and_rank_hist()
        for val in self.ranks.values():
            if val >= 4:
                return True
        return False

    def has_straight_flush(self):
        self.suit_and_rank_hist()
        cards_of_one_suit = []


if __name__ == '__main__':
    # make a deck
    deck = Deck()
    deck.shuffle()

    # deal the cards and classify the hands
    for i in range(7):
        hand = PokerHand()
        deck.move_cards(hand, 7)
        hand.sort()
        print(hand)
        print(hand.has_full_house())
        print('')

