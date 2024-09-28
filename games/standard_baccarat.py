from classes import Shoe

class StandardBaccaratGame:
    def __init__(self, shoe: Shoe):
        self.shoe = shoe
        self.player_hand = []
        self.banker_hand = []

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

    def player_draws(self):
        player_total = self.get_hand_total(self.player_hand)
        if player_total <= 5:  # Player draws a card
            self.player_hand.append(self.shoe.deal_card())

    def banker_draws(self, player_third_card=None):
        banker_total = self.get_hand_total(self.banker_hand)
        if banker_total <= 2:
            self.banker_hand.append(self.shoe.deal_card())
        elif banker_total == 3 and player_third_card not in [8]:  # Player's third card cannot be 8
            self.banker_hand.append(self.shoe.deal_card())
        elif banker_total == 4 and player_third_card in [2, 3, 4, 5, 6, 7]:
            self.banker_hand.append(self.shoe.deal_card())
        elif banker_total == 5 and player_third_card in [4, 5, 6, 7]:
            self.banker_hand.append(self.shoe.deal_card())
        elif banker_total == 6 and player_third_card in [6, 7]:
            self.banker_hand.append(self.shoe.deal_card())
        # If banker_total is 7, banker stands

    def play_round(self):
        self.deal_initial_cards()
        player_total = self.get_hand_total(self.player_hand)
        print(f"{self.player_hand=} {player_total=}")
        banker_total = self.get_hand_total(self.banker_hand)
        print(f"{self.banker_hand=} {banker_total=}")
        # Player logic
        if player_total <= 5:
            print("Drawing player card")
            self.player_draws()
        
        # Banker's third card logic
        player_third_card = self.player_hand[2] if len(self.player_hand) > 2 else None
        self.banker_draws(player_third_card)

        # Show the results
        print(f"Player Hand: {[(card.name, card.value) for card in self.player_hand]} Total: {player_total}")
        print(f"Banker Hand: {[(card.name, card.value) for card in self.banker_hand]} Total: {self.get_hand_total(self.banker_hand)}")
