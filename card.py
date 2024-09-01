#!/usr/bin/env python3

from random import randint

class Deck:
    
    def __init__(self):
        self.suits = ("spades", "clubs", "hearts", "diamonds")
        self.numbers = [1,2,3,4,5,6,7,8,9,10,"J","Q","K","A"]
        deck = {}

        for suit in self.suits:
            deck[suit] = self.numbers
        
        self.deck = deck


class Card(Deck):

    @classmethod
    def pick_card(Card):

        random_suit = Deck().suits[randint(0,3)]
        random_num = Deck().numbers[randint(0,len(Deck().numbers)-1)]
        
        card = (random_suit, random_num)

        print(card)
