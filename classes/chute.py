from playingcards import Card, Deck
from classes import Shuffler

# 6-8 deck_count
class Chute:
    def __init__(self, deck_count: int = 8, shuffle_type: str = "HAND", cut_position: int = -1):
        self.cards = self._generate_chute(deck_count, shuffle_type)
        self.total_cards = len(self.cards)  # Total number of cards in the chute
        self.game_in_progress = False

        self.cut_position = cut_position if cut_position != -1 else self.total_cards
        self.deal_index = 0  # Pointer to track the current card being dealt

    def _generate_chute(self, deck_count: int, shuffle_type: str = "HAND"):
        """Generate and shuffle the chute with the specified number of decks."""
        if shuffle_type == "HAND":
            return [self._shuffle_deck(Deck().cards) for _ in range(deck_count)]
        if shuffle_type == "ELECTRONIC":
            return self._shuffle_deck([Deck().cards for _ in range(deck_count)])
        return [Deck().cards for _ in range(deck_count)]

    def _shuffle_deck(self, deck):
        """Shuffle a single deck or a list of decks."""
        shuffler = Shuffler(cards=deck)
        shuffler.shuffle()
        return deck

    def deal_card(self):
        """Deal one card from the chute and track how many cards have been dealt."""
        if self.deal_index >= len(self.cards):
            raise Exception("No more cards in the chute.")
        
        # Deal the card at the current index, without modifying the list
        card = self.cards[self.deal_index]
        self.deal_index += 1  # Move the pointer to the next card
        
        return card