import random

def overhand_shuffle(deck):
    shuffled_deck = []
    while deck:
        chunk_size = random.randint(1, len(deck) // 4)
        chunk = deck[:chunk_size]
        deck = deck[chunk_size:]
        shuffled_deck = chunk + shuffled_deck
    return shuffled_deck