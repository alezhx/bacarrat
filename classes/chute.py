from playingcards import Card

class Chute:
    def __init__(self, ordered: bool=False):
        self.ordered = ordered

    def generate_chute(self, decks: int, ordered: bool = False):
        pass

    def remove_card(self, position):
        self.cards.pop(position)

    def order_cards(self):
        if not self.ordered:
            self.cards.sort()
            self.ordered = True