#!/usr/bin/env python3

from card import Deck, Card

if __name__ == '__main__':
    card = Card().pick_card()
    deck = Deck().deck

    print(card, "\n\n", deck)
