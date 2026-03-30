# Assignment 2 - Card Draw 
# Author: Maroua EL imame 

# Deck of Cards API (https://deckofcardsapi.com) : an API that simulates dealing a deck of cards

# In this program, 5 cards are drawn and printed
# -  1: a new deck is shuffled, the API response includes a 'deck_id' which uniquely identifies the deck and is used to draw cards in the next steps. 
# -  2: using the 'deck_id', cards are drawn from the deck then a value (rank) and a suit (category) of each card are displayed. 
# -  3: the program checks whether Pair, Three of a Kind, Straight, or Flusha have been drawn then congratulates the user accordingly.   



# 1. create and shuffle a new deck

import requests
url = "https://deckofcardsapi.com/api/deck/new/shuffle/?deck_count=1"
response = requests.get(url)
data = response.json()


deck_id = data["deck_id"]
print("\nDeck ID:", deck_id)
print("\nCards remaining:", data["remaining"])

print("-------------------")
# 2. draw five cards
draw_url = f"https://deckofcardsapi.com/api/deck/{deck_id}/draw/?count=5"
response = requests.get(draw_url)
draw_data = response.json()

print("\nDrawn cards:\n")

for card in draw_data["cards"]:
    print(card["value"], "of", card["suit"])

print("-------------------")

# 3. check the hand

cards = draw_data["cards"]

values = [card["value"] for card in cards]
suits = [card["suit"] for card in cards]

# count values
counts = [values.count(v) for v in values]

# checks
has_triple = 3 in counts
has_pair = 2 in counts
#flush
has_flush = len(set(suits)) == 1                            # set() removes duplicates, if only one suit then length is 1
# straight
order = ["ACE","2","3","4","5","6","7","8","9","10","JACK","QUEEN","KING"]
nums = sorted(order.index(v) for v in values)
has_straight = nums == list(range(nums[0], nums[0] + 5))    # convert card values to their positions and check if they form a consecutive sequence (straight)


# results
if has_triple:
    print("\nNo way!!! Three of a kind!\n")
elif has_pair:
    print("\nNice work! You hit a pair!\n")

if has_flush:
    print("\nWhat a hand! That's a flush!\n")

if has_straight:
    print("Unreal! Straight!\n")

if not any([has_triple, has_pair, has_flush, has_straight]):
    print("\nTough hand, try again!\n")