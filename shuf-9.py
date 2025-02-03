# 9. Python Program to Shuffle Deck of Cards

import itertools
import random

suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']

deck = list(itertools.product(ranks, suits))
random.shuffle(deck)
print("Shuffled deck of cards:")
for card in deck:
    print(f"{card[0]} of {card[1]}")