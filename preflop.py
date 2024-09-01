#!/usr/bin/env python3

from card import Deck

class Shuffle:

    def __init__(self, people=8):
        self.people = people
        
    def cards_preflop(self):
        
        deck = Deck()
        pre = {}
        for person in range(self.people):
            pre[person+1] = list(deck.pick_card() for _ in range(2))

        return pre
