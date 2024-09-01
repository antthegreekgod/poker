#!/usr/bin/env python3

from card import Deck
from preflop import Shuffle

if __name__ == '__main__':
    shuff = Shuffle().cards_preflop()

    print(shuff)
