from playingcards import Card as Card_


class Card(Card_):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    @property
    def short_name(self):
        return ""