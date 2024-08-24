from shuffles.riffle_shuffle import riffle_shuffle
from shuffles.overhand_shuffle import overhand_shuffle
from shuffles.faro_shuffle import faro_shuffle
from shuffles.fisher_yates_shuffle import fisher_yates_shuffle

def simulate_shuffle(cards):
    cards = riffle_shuffle(cards)
    cards = faro_shuffle(cards)
    cards = riffle_shuffle(cards)
    cards = overhand_shuffle(cards)
    cards = fisher_yates_shuffle(cards)
    cards = riffle_shuffle(cards)

    return cards