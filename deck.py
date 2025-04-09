heart_deck = [] #total card number list
count1 = 0 
card1 = 2
#initialize all variables for hearts

while count1 < 9:
    nameCard1 = f"{card1} of Hearts"
    heart_deck.append(nameCard1)
    card1 += 1
    count1 += 1
#while loop that adds card3 values to string list heart_deck

faceHearts = ['Ace of Hearts', 'Jack of Hearts', 'Queen of Hearts', 'King of Hearts']
heart_deck.insert(0, faceHearts[0])
heart_deck.insert(count1+1, faceHearts[1])
heart_deck.insert(count1+2, faceHearts[2])
heart_deck.insert(count1+3, faceHearts[3])

spade_deck = [] #total card2 number list
count2 = 0 
card2 = 2
#initialize all variables for spades

while count2 < 9:
    nameCard2 = f"{card2} of Spades"
    spade_deck.append(nameCard2)
    card2 += 1
    count2 += 1
#while loop that adds card3 values to string list spade_deck

faceSpades = ['Ace of Spades', 'Jack of Spades', 'Queen of Spades', 'King of Spades']
spade_deck.insert(0, faceSpades[0])
spade_deck.insert(count2+1, faceSpades[1])
spade_deck.insert(count2+2, faceSpades[2])
spade_deck.insert(count2+3, faceSpades[3])

diamond_deck = [] #total card3 number list
count3 = 0 
card3 = 2
#initialize all variables

while count3 < 9:
    nameCard3 = f"{card3} of Diamonds"
    diamond_deck.append(nameCard3)
    card3 += 1
    count3 += 1
#while loop that adds card3 values to string list diamond_deck

faceDiamonds = ['Ace of Diamonds', 'Jack of Diamonds', 'Queen of Diamonds', 'King of Diamonds']
diamond_deck.insert(0, faceDiamonds[0])
diamond_deck.insert(count3+1, faceDiamonds[1])
diamond_deck.insert(count3+2, faceDiamonds[2])
diamond_deck.insert(count3+3, faceDiamonds[3])

club_deck = [] #total card4 number list
count4 = 0 
card4 = 2
#initialize all variables

while count4 < 9:
    nameCard4 = f"{card4} of Clubs"
    club_deck.append(nameCard4)
    card4 += 1
    count4 += 1
#while loop that adds card values to string list heart_deck

faceClubs = ['Ace of Clubs', 'Jack of Clubs', 'Queen of Clubs', 'King of Clubs']
club_deck.insert(0, faceClubs[0])
club_deck.insert(count4+1, faceClubs[1])
club_deck.insert(count4+2, faceClubs[2])
club_deck.insert(count4+3, faceClubs[3])


cardDeck = []
plus = 0
while plus < 13:
    cardDeck.append(heart_deck[plus])
    cardDeck.append(diamond_deck[plus])
    cardDeck.append(club_deck[plus])
    cardDeck.append(spade_deck[plus])
    plus += 1
#assign values of types to entire deck list

print("Here's the entire deck:")
for card in cardDeck[:]:
    print(card)
#for loop printing all cards in deck

print("\nHere are only the Spade cards:")
for card in range(3,52,4):
    print(cardDeck[card])
#for loop and range function used for printing only the spade cards in cardDeck

#OLD CODE*******
# count = 0 
# while count < 52:
#     print (cardDeck[count])
#     count += 1
#print values of entire deck