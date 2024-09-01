#!/usr/bin/env python3

from random import randint

class Deck:
    
    def __init__(self):
        self.suits = ("spades", "clubs", "hearts", "diamonds")
        self.numbers = (2,3,4,5,6,7,8,9,10,"J","Q","K","A")
        self.deck = [0]*52

        i = 0
        for suit in self.suits:
            for num in self.numbers:
                self.deck[i] = (suit,num)
                i+=1

    def pick_card(self):

        card = self.deck[randint(0,len(self.deck)-1)]
        self.deck.remove(card)

        return card
