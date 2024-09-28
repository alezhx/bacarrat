import random

def overhand_shuffle(deck):
    shuffled_deck = []
    while deck:
        # Ensure chunk_size is at least 1 and at most len(deck)
        chunk_size = random.randint(1, max(1, len(deck) // 4))
        chunk = deck[:chunk_size]
        deck = deck[chunk_size:]
        shuffled_deck = chunk + shuffled_deck
    return shuffled_deck