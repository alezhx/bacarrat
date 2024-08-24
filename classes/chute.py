from playingcards import Card

# 6-8 decks
class Chute:
    def __init__(self, decks: int=8, ordered: bool=False):
        self.__validate_params
        self.ordered = ordered

    def generate_chute(self, decks: int, ordered: bool = False):
        pass

    def remove_card(self, position):
        self.cards.pop(position)

    def order_cards(self):
        if not self.ordered:
            self.cards.sort()
            self.ordered = True