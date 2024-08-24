def faro_shuffle(deck):
    half = len(deck) // 2
    left = deck[:half]
    right = deck[half:]
    
    shuffled_deck = []
    for l, r in zip(left, right):
        shuffled_deck.append(l)
        shuffled_deck.append(r)
        
    return shuffled_deck