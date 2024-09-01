#!/usr/bin/env python3

from card import Deck
from preflop import Shuffle
from counter import Count

def main(num_games):
    pairs = 0
    for num in range(num_games):
        if game():
            pairs +=1

    print(f"\nThe probability of recieving one pair in a preflop is: {pairs/num_games*100}%\n") # result

def game():
    shuff = Shuffle().cards_preflop() # preflop cards for 1 game
    my_player = shuff[1] # only store pair of cards of player 1
    outcome = Count(my_player) 
    return outcome.is_pair() # returns False or True if pair

if __name__ == '__main__':
    main(100000)
