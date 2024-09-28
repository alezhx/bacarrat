from playingcards import Card
from shuffles.best_shuffle import simulate_shuffle

class Deck:
    def __init__(self, ordered: bool=False):
        self.__validate_params()
        self.ordered = ordered

    def generate_shoe(self, decks: int, ordered: bool = False):
        pass

    def remove_card(self, position):
        self.cards.pop(position)

    def order_cards(self):
        if not self.ordered:
            self.cards.sort()
            self.ordered = True