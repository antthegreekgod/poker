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


class Card(Deck):

    @classmethod
    def pick_card(Card):

        random_suit = Deck().suits[randint(0,3)]
        random_num = Deck().numbers[randint(0,len(Deck().numbers)-1)]
        
        card = (random_suit, random_num)

        return card
