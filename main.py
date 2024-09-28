import random
import math
from classes import Shoe, Card
from games import StandardBaccaratGame

# class BaccaratConfig():
#     def __init__(self) *> None:
        

def prepare_bacarrat_shoe(deck_count=8, shuffle_type="HAND"):
    # Generate random cut position
    total_num_cards = deck_count*52
    cut_randomness = random.uniform(0.7,1.0)
    cut_position = math.floor(total_num_cards*cut_randomness)

    shoe = Shoe(deck_count, shuffle_type)
    # Insert cut card
    shoe.add_cut_card(cut_position)

    return shoe

# from typing import Callable
# def standard_variation_game(shoe: Shoe):
#     card = shoe.deal_card()
#     print(card.name)
#     print(card.img)


def baccarat(config={}):
    print("Begin Baccarat")
    shoe = prepare_bacarrat_shoe(deck_count=8)

    game_count = 0
    while True:
        try:
            print("**********************************************************************")
            print(f"Starting Game {game_count}")
            game = StandardBaccaratGame(shoe=shoe)
            result = game.play_round()
            print(f"Finished Game {game_count}: {result.value}")
            print("**********************************************************************")
            game_count+=1
        except Exception as e:
            print(e)
            raise e
    
baccarat()
