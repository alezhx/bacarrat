import random
from shuffles import faro_shuffle, fisher_yates_shuffle, overhand_shuffle, riffle_shuffle

class Shuffler:
    def __init__(self, cards):
        self.cards = cards

    def shuffle_v1(self):
        shuffle_order = [
            fisher_yates_shuffle,
            faro_shuffle,
            riffle_shuffle,
            overhand_shuffle,
            riffle_shuffle,
            fisher_yates_shuffle,
        ]
        # print("start", len(self.cards), self.cards)
        for _ in range(random.randint(6, 9)):
            for shuffle in shuffle_order:
                self.cards = shuffle(self.cards)
        # print("end", len(self.cards), self.cards)
    def shuffle(self):
        shuffle_order = [
            fisher_yates_shuffle,
            faro_shuffle,
            riffle_shuffle,
            overhand_shuffle,
        ]
        
        # Randomize the shuffle order
        random.shuffle(shuffle_order)
        
        # Shuffle the cards a random number of times
        for _ in range(random.randint(6, 9)):
            for shuffle in shuffle_order:
                self.cards = shuffle(self.cards)