import random
import math
from classes import Card, Shoe

# class BaccaratConfig():
#     def __init__(self) -> None:
        

def prepare_bacarrat_shoe(deck_count=8, shuffle_type="HAND"):
    # Generate random cut position
    total_num_cards = deck_count*52
    cut_randomness = random.uniform(0.7,1.0)
    cut_position = math.floor(total_num_cards*cut_randomness)

    shoe = Shoe(deck_count, shuffle_type)
    # Insert cut card
    shoe.add_cut_card(cut_position)

    return shoe


def baccarat(config={}):
    shoe = prepare_bacarrat_shoe()

    while True:
        try:
            card = shoe.deal_card()
            print(card)
        except Exception as e:
            print(e)
    

