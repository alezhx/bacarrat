import random

def fisher_yates_shuffle(deck):
    for i in range(len(deck)-1, 0, -1):
        j = random.randint(0, i)
        deck[i], deck[j] = deck[j], deck[i]
    return deck