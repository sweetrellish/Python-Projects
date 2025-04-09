from hearts import heart_deck
from diamonds import diamond_deck
from clubs import club_deck
from spades import spade_deck
from random import randrange
#import all card types

cardDeck = []
plus = 0
while plus < 13:
    cardDeck.append(heart_deck[plus])
    cardDeck.append(diamond_deck[plus])
    cardDeck.append(club_deck[plus])
    cardDeck.append(spade_deck[plus])
    plus += 1
#assign values of types to entire deck list

print("\n\nHere's the entire deck:")
count = 0 
while count < 52:
    print (cardDeck[count])
    count += 1
#print values of entire deck

print("Here's your starting hand:\n")

deal = 0
while deal < 5:
    print(cardDeck[randrange(52)])
    deal += 1
# deal hand of random cards from the deck


