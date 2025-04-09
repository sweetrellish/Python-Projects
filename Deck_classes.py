"""Module containing functions that relate to card and deck manipulation"""
class Deck:
    """Class defining a deck of cards, and contains methods of deck functions"""
    def __init__(self):
        self.values = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        self.suits = ['♠','♥','♦','♣']
        self.cardValues = {"A": 11,"2": 2,"3": 3,"4": 4,"5": 5,"6": 6,"7": 7,"8": 8,"9": 9,"10": 10,"J": 10,"Q": 10,"K": 10}
        
        deck = []
        for suit in self.suits:
            for value in self.values:
                card = value + suit
                deck.append(card)

        self.deck = deck
    #creates deck   
    def deal_top_card(self):
        """Takes deck argument and returns top card value and removes from the deck"""
        card = self.deck.pop(0)
        return card
    #returns top card from deck

    def get_random_card(self):
        """Given argument deck, returns random card in deck."""
        from random import randrange
        num = randrange(52)
        card = self.deck.pop(num)
        return card
    #returns random card from the deck, removes from deck

    def shuffle_deck(self):
        """Takes deck argument and returns shuffled deck."""
        import random
        random.shuffle(self.deck)
        return self.deck
    #shuffles deck

    def deal_hands(self, hand_num, hands = 1):
        """Takes deck, hand amount and number of hands and returns the hands."""
        wcount = 0
        fcount = 0
    
        new_hands = {}
    
        while wcount < hands:
            for card in range(hand_num):     
                card = self.deck.pop(fcount)
                new_hands[f'{wcount}'].append(card)
                fcount += 1
            wcount += 1
        return new_hands
    #deals multiple hands  

    def deal_hand(self, hand):
        """Takes argument for one hand only and returns hand."""
        new_hand =[]
        for card in range(hand):
            new_hand.append(self.deck.pop(card))
        return new_hand
    #deals hand to user/computer, removes cards from deck

    def get_suit(self, card):
        suit = card[-1]
        return suit
    #returns suit of card

    def same_Value(self, card1, card2):
        """Takes number of cards and tests value equivalency of each card."""
        value1 = card1[0]
        value2 = card2[0]
        if value1 == value2:
            return True
        else:
            return False
    #checks if card values are equivalent

    def same_Suit(self, card1, card2):
        """Takes suit of cards and tests equivalency of each card."""
        suit1 = card1[-1]
        suit2 = card2[-1]
        if suit1 == suit2:
            return True
        else:
            return False
    #checks if card suits are equivalent

    def get_Value(self, card):
            """Takes in card argument and returns number value of that card."""
            value = card[0]
            return value
    #returns value of card number
    def hand_pairs(self, hand1, hand2):
        """Takes in 2 hand arguments and checks for pairs"""
        pair =[]      

        for cards in hand1:                      #nested for loop to check value and ensure true pair, could act as method for handPairs(), adds to pair list and removes from hand
            for clone in hand2:              
                    if self.get_Value(cards) == self.get_Value(clone) and self.get_suit(cards) != self.get_suit(clone):
                        pair.append(cards)
                        pair.append(clone)
                        hand1.remove(cards)
                        hand2.remove(clone)
                        # hand1.remove(cards)
                        # hand1.remove(clone)
                        print(f"Storing {cards, clone} into pairs...")  
                    
        if pair:
            print(f'Pairs: {pair}\n')
        else:
            print('You have no pairs.\n')
        return pair

    def empty_hand(self, hand):
        """Tests whether a hand is empty"""
        if hand:
            return False
        else:
            return True
    def hand_random_card(self, hand):
        """Selects a random card from the hand to ask for in 'Go-Fish' """
        import random
        import card_functions
        random.shuffle(hand)
        card = hand.pop(0)
        hand.append(card)
        return card_functions.get_Value(card)

    def hand_Value(self, hand, ace):
        """Takes in card argument and returns value of card"""
        cardValues = {"A": 11,"2": 2,"3": 3,"4": 4,"5": 5,"6": 6,"7": 7,"8": 8,"9": 9,"10": 10,"J": 10,"Q": 10,"K": 10}
        num = 0
        for card in hand:
            if ace == 'high':
                cardValues["A"] = 11
            elif ace == 'low':
                cardValues["A"] = 1
            num += cardValues[f"{self.get_Value(card)}"]

        return num
    def number_of_cards(self, hand):
        """Takes in hand argument and returns number of cards in hand"""
        count = 0
        for card in hand:
            count += 1
        return count