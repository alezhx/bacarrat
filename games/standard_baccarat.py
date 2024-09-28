from classes import Shoe
from enum import Enum

class GameOutcome(Enum):
    BANKER_WIN = "BANKER_WIN"
    PLAYER_WIN = "PLAYER_WIN"
    TIE = "TIE"

class StandardBaccaratGame:
    def __init__(self, shoe: Shoe):
        self.shoe = shoe
        self.player_hand = []
        self.banker_hand = []

    @property
    def player_total(self):
        return self.get_hand_total(self.player_hand)

    @property
    def banker_total(self):
        return self.get_hand_total(self.banker_hand)

    def deal_initial_cards(self):
        # Deal two cards to both player and banker
        for _ in range(2):
            self.player_hand.append(self.shoe.deal_card())
            self.banker_hand.append(self.shoe.deal_card())

    def get_baccarat_value(self, card):
        if card.value > 10:
            return 10
        return card.value

    def get_hand_total(self, hand):
        total = sum(self.get_baccarat_value(card) for card in hand) % 10
        return total

    def handle_player_draws(self):
        if self.player_total <= 5:  # Player draws a card
            print("Player: DRAW_THIRD")
            self.player_hand.append(self.shoe.deal_card())
    
    def handle_banker_draws(self):
        draw_conditions = (
            self.banker_total <= 2 or
            (self.banker_total == 3 and self.player_total not in [8]) or
            (self.banker_total == 4 and self.player_total in [2, 3, 4, 5, 6, 7]) or
            (self.banker_total == 5 and self.player_total in [4, 5, 6, 7]) or
            (self.banker_total == 6 and self.player_total in [6, 7])
        )
        
        if draw_conditions:
            print("Banker: DRAW_THIRD")
            self.banker_hand.append(self.shoe.deal_card())
        # If banker_total is 7, banker stands

    def determine_winner(self):
        if self.player_total > self.banker_total:
            return GameOutcome.PLAYER_WIN
        elif self.banker_total > self.player_total:
            return GameOutcome.BANKER_WIN
        else:
            return GameOutcome.TIE

    def play_round(self):
        self.deal_initial_cards()

        print("----------------------------------------------------------------------initial deal phase")
        print(f"(P): {[card.name for card in self.player_hand]} Total: {self.player_total}")
        print(f"(B): {[card.name for card in self.banker_hand]} Total: {self.banker_total}")

        # Check for naturals before drawing any cards
        if self.player_total in [8, 9] or self.banker_total in [8, 9]:
            print("Natural! No further draws.")
            return self.determine_winner()
        # Player logic for drawing

        print("----------------------------------------------------------------------additional deal phase")
        self.handle_player_draws()
        self.handle_banker_draws()

        # Show the results
        print(f"(P): {[card.name for card in self.player_hand]} Total: {self.player_total}")
        print(f"(B): {[card.name for card in self.banker_hand]} Total: {self.banker_total}")

        return self.determine_winner()
