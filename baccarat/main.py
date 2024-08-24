from playingcards import Card

class BaccaratChute:
    def __init__(self, cards=None, maximum: int = None, ordered: bool = False) -> None:
        self.cards = cards
        self.maximum = maximum
        self.ordered = ordered