from playingcards import Card, Deck
from classes import Shuffler

# 6-8 deck_count
class Chute:
    def __init__(self, deck_count: int=8, shuffle_type: str="HAND", cut_position: int=-1):
        self.chute = self.generate_chute(self, deck_count, shuffle_type)
        self.cut_position = cut_position
        # self.__validate_params(self.chute)

    def generate_chute(self, deck_count: int, shuffle_type: str="HAND"):
        if shuffle_type == "HAND":
            return [self.shuffle(Deck()) for _ in range(deck_count)]
        if shuffle_type == "ELECTRONIC":
            return self.shuffle([Deck() for _ in range(deck_count)])
        
        return [Deck() for _ in range(deck_count)]
    
    def shuffle(self, cards: list):
        shuffler = Shuffler(cards=cards)
        shuffler.shuffle()
        return cards



    def remove_card(self, position):
        self.chute.pop(position)

    def order_chute_cards(self):
        if not self.ordered:
            self.chute_cards.sort()
            self.ordered = True
