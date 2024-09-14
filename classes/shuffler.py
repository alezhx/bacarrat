import random
from shuffles import faro_shuffle, fisher_yates_shuffle, overhand_shuffle, riffle_shuffle

class Shuffler:
    def __init__(self, cards):
        self.cards = cards

    # def riffle_shuffle(self):
    #     mid = len(self.cards) // 2
    #     left = self.cards[:mid]
    #     right = self.cards[mid:]
    #     shuffled = []
    #     while left or right:
    #         if random.random() > 0.5 and left:
    #             shuffled.append(left.pop(0))
    #         elif right:
    #             shuffled.append(right.pop(0))
    #     self.cards = shuffled

    # def overhand_shuffle(self):
    #     num_chunks = random.randint(8, 12)
    #     chunk_size = len(self.cards) // num_chunks
    #     shuffled = []
    #     for i in range(num_chunks):
    #         chunk = self.cards[i*chunk_size:(i+1)*chunk_size]
    #         random.shuffle(chunk)
    #         shuffled.extend(chunk)
    #     self.cards = shuffled

    # def fisher_yates_shuffle(self):
    #     for i in range(len(self.cards) - 1, 0, -1):
    #         j = random.randint(0, i)
    #         self.cards[i], self.cards[j] = self.cards[j], self.cards[i]

    # def faro_shuffle(self, in_shuffle=True):
    #     half = len(self.cards) // 2
    #     left = self.cards[:half]
    #     right = self.cards[half:]
    #     shuffled = []
    #     if in_shuffle:
    #         for l, r in zip(left, right):
    #             shuffled.append(r)
    #             shuffled.append(l)
    #         if len(left) > len(right):
    #             shuffled.append(left[-1])
    #     else:
    #         for l, r in zip(left, right):
    #             shuffled.append(l)
    #             shuffled.append(r)
    #         if len(left) > len(right):
    #             shuffled.append(left[-1])
    #     self.cards = shuffled

    def shuffle(self):
        shuffle_order = [
            fisher_yates_shuffle,
            faro_shuffle,
            riffle_shuffle,
            overhand_shuffle,
            riffle_shuffle,
            fisher_yates_shuffle,
        ]
        for shuffle in shuffle_order:
            self.cards = shuffle(self.cards)
