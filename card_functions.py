def build_deck():
    """Builds a deck with for loops and lists,
       And returns list of cards in order"""
    deck = []
    suits = ['♠','♥','♦','♣']
    values = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
    
    for suit in suits:
        for value in values:
            card = value + suit
            deck.append(card)
    return deck  
#creates deck   

def get_suit(card):
    suit = card[-1]
    return suit
#returns suit of card

def same_Value(card1, card2):
    """Takes number of cards and tests value equivalency of each card."""
    value1 = card1[0]
    value2 = card2[0]
    if value1 == value2:
        return True
    else:
        return False
#checks if card values are equivalent

def same_Suit(card1, card2):
    """Takes suit of cards and tests equivalency of each card."""
    suit1 = card1[-1]
    suit2 = card2[-1]
    if suit1 == suit2:
        return True
    else:
        return False
#checks if card suits are equivalent

def get_Value(card):
        """Takes in card argument and returns number value of that card."""
        value = card[0]
        return value
 #returns value of card number

#TEST CODE

# deck = build_deck()
# print(same_Value('2♣', '2♣'))
# print(deck)
# suit = get_suit('2♣')
# print(suit)
# value = get_Value('J♥')
# print(value)
# print(same_Value('2♥', '3♥'))
# print(same_Suit('2♥', '2♣'))

#All functions are working as needed 4/13/2022
#CHARACTERS FOR SUITS: ♠ ♥ ♦ ♣