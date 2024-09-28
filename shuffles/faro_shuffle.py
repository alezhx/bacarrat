import random

def faro_shuffle(cards: list, in_shuffle: bool = None):
    half = len(cards) // 2  # Use integer division to get the correct half
    left = cards[:half]
    right = cards[half:]
    shuffled = []

    if in_shuffle is None:
        in_shuffle = random.choice([True, False])

    if in_shuffle:
        # In-shuffle: Interleave starting with the second half
        for l, r in zip(left, right):
            shuffled.append(r)
            shuffled.append(l)
        if len(right) > len(left):  # Handle odd-length cards
            shuffled.append(right[-1])
    else:
        # Out-shuffle: Interleave starting with the first half
        for l, r in zip(left, right):
            shuffled.append(l)
            shuffled.append(r)
        if len(left) > len(right):  # Handle odd-length cards
            shuffled.append(left[-1])

    return shuffled