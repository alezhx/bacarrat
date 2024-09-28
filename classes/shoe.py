from playingcards import Deck
from collections import Counter

# 6-8 deck_count
class Shoe:
    def __init__(self, deck_count: int = 8, shuffle_type: str = "HAND"):
        self.cards = self._generate_shoe(deck_count, shuffle_type)
        self.total_cards = len(self.cards)  # Total number of cards in the shoe
        print(f"{self.total_cards=}")
        # self.cut_position = self.total_cards
        self.deal_index = 0  # Pointer to track the current card being dealt

        # Validate the shoe after generation
        self._validate_shoe(deck_count)

    def _generate_shoe(self, deck_count: int, shuffle_type: str = "HAND"):
        """Generate and shuffle the shoe with the specified number of decks."""
        base_deck = Deck().cards  # Get the base deck once
        # shuffle_type = "asdasdadasd"
        if shuffle_type == "HAND":
            # Create the shoe by repeating and shuffling the base deck
            shoe = base_deck * deck_count  # Create a list with deck_count decks
            return self._shuffle_deck(shoe)  # Shuffle the combined list

        if shuffle_type == "ELECTRONIC":
            # Create and shuffle a full shoe
            return self._shuffle_deck(base_deck * deck_count)

        # Default case if shuffle_type is not recognized
        return base_deck * deck_count  # Just repeat the base deck


    def _shuffle_deck(self, deck):
        """Shuffle a single deck or a list of decks."""
        from classes import Shuffler
        shuffler = Shuffler(cards=deck)
        shuffler.shuffle()
        return shuffler.cards
    
    def add_cut_card(self, cut_position):
        """Inject "X_CARD" into the list of cards at the specified cut position."""
        if cut_position < 0 or cut_position > self.total_cards:
            raise IndexError("Cut position out of bounds.")

        self.cards.insert(cut_position, "X_CARD")  # Insert "X_CARD" at the specified position

    def deal_card(self):
        """Deal one card from the shoe and track how many cards have been dealt."""
        if self.deal_index >= len(self.cards):
            raise Exception("No more cards in the shoe.")
        
        # Deal the card at the current index, without modifying the list
        card = self.cards[self.deal_index]
        self.deal_index += 1  # Move the pointer to the next card
        
        return card
    
    def _validate_shoe(self, deck_count: int):
        """Validate the generated shoe to ensure it contains the correct counts of all expected cards."""
        base_deck = Deck().cards
        expected_count = deck_count# Each card type 1/52 should be seen deck_count times

        actual_count = Counter([str(c) for c in self.cards])  # Count occurrences of each card in the shoe

        for card in base_deck:
            card_str = str(card)
            if actual_count[card_str] != expected_count:
                raise ValueError(f"Incorrect count for {card_str}: expected {expected_count}, found {actual_count[card_str]}.")