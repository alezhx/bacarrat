import random

def riffle_shuffle_deck(deck):
    # Split the deck into two halves
    mid = len(deck) // 2
    left = deck[:mid]
    right = deck[mid:]
    
    shuffled_deck = []
    while left or right:
        if left and (not right or random.random() > 0.5):
            shuffled_deck.append(left.pop(0))
        if right and (not left or random.random() > 0.5):
            shuffled_deck.append(right.pop(0))
    
    return shuffled_deck

def riffle_shuffle(deck, times=7):
    for _ in range(times):
        deck = riffle_shuffle(deck)
    return deck
