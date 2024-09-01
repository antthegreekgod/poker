#!/usr/bin/env python3

class Count:

    def __init__(self, cards):
        self.cards = cards

    def is_pair(self):
        if self.cards[0][1] == self.cards[1][1]:
            return True
        else:
            return False

        

