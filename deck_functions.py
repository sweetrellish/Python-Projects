import card_functions
def deal_top_card(deck):
    """Takes deck argument and returns top card value and removes from the deck"""
    card = deck.pop(0)
    return card

def get_random_card(deck):
    """Given argument deck, returns random card in deck."""
    from random import randrange
    num = randrange(0, len(deck)-1)
    card = deck.pop(num)
    return card

def shuffle_deck(deck):
    """Takes deck argument and returns shuffled deck."""
    import random
    random.shuffle(deck)
    return deck

def deal_hands(deck, hand_num, hands = 1):
    """Takes deck, hand amount and number of hands and returns the hands."""
    wcount = 0
    fcount = 0
    new_hand = []
    while wcount < hands:
        for card in range(hand_num):     
            card = deck.pop(fcount)
            new_hand.append(card)
            fcount += 1
        wcount += 1
    return new_hand
    

def deal_hand(deck, hand):
    """Takes argument for one hand only and returns hand."""
    new_hand =[]
    for card in range(hand):
        new_hand.append(deck.pop(card))
    return new_hand

def hand_pairs(hand1, hand2):
    """Takes in 2 hand arguments and checks for pairs"""
    pair =[]   

    for i, cards in enumerate(hand1):                      #nested for loop to check value and ensure true pair, could act as method for handPairs(), adds to pair list and removes from hand
        for j, clone in enumerate(hand2):              
                if card_functions.get_Value(cards) == card_functions.get_Value(clone) and card_functions.get_suit(cards) != card_functions.get_suit(clone):
                    hand1.pop(i)
                    hand2.pop(j)
                    if cards in pair and clone in pair:
                        break
                    pair.append(cards)
                    pair.append(clone)
                    
                    print(f"Storing {cards, clone} into pairs...")  
                
    if pair:
        print(f'Pairs: {pair}\n')
    else:
        print('You have no pairs.\n')
    return pair

def empty_hand(hand):
    """Tests whether a hand is empty"""
    if hand:
        return False
    else:
        return True
def hand_random_card(hand):
    """Selects a random card from the hand to ask for in 'Go-Fish' """
    import random
    import card_functions
    random.shuffle(hand)
    card = hand.pop(0)
    hand.append(card)
    return card_functions.get_Value(card)

def hand_Value(hand, ace):
    """Takes in card argument and returns value of card"""
    cardValues = {"A": 11,"2": 2,"3": 3,"4": 4,"5": 5,"6": 6,"7": 7,"8": 8,"9": 9,"10": 10,"J": 10,"Q": 10,"K": 10}
    num = 0
    for card in hand:
        if ace == 'high':
            cardValues["A"] = 11
        elif ace == 'low':
            cardValues["A"] = 1
        num += cardValues[f"{card_functions.get_Value(card)}"]

    return num
def number_of_cards(hand):
    """Takes in hand argument and returns number of cards in hand"""
    count = 0
    for card in hand:
        count += 1
    return count



#TEST CODE
# from card_functions import build_deck
# ace1 = 'high'
# deck = build_deck()
# print(deck)

# shuffle_deck(deck)
# print(deck)

# print(deal_top_card(deck))
# print(get_random_card(deck))
# hand1 = deal_hand(deck, 7)
# print(hand1)
# print(hand_Value(hand1, ace1))

# print(deal_hands(deck, 7))

#All functions are working as needed 4/13/22
#CHARACTERS FOR SUITS: ♠ ♥ ♦ ♣