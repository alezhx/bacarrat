from playingcards import Deck as Deck_
from . import card

class Deck(Deck_):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.cards = [card.Card(value=c.value, suit=c.suit, deck=self) for c in self.cards]
