face_cards = {'Jack': '', 'Queen': '', 'King': '', 'Ace': ''}
suits = { 
    'Hearts': {}, 
    'Spades': {},
    'Clubs' : {}, 
    'Diamonds': {}
}
#create dictionaries to store card values

deck = []
#list deck to store all values

for suit in suits:
    for card in range(2,11):
        if suit == 'Hearts':
            suits['Hearts'] = f'{card} of Hearts'
           # print(suits[suit])
            deck.append(suits[suit])
        elif suit == 'Spades':
            suits['Spades'] = f'{card} of Spades'
           # print(suits[suit])
            deck.append(suits[suit])
        elif suit == 'Clubs':
            suits['Clubs'] = f'{card} of Clubs'
            #print(suits[suit])
            deck.append(suits[suit])
        elif suit == 'Diamonds':
            suits['Diamonds'] = f'{card} of Diamonds'
           # print(suits[suit])
            deck.append(suits[suit])
#nested for loop to store all number cards

for face in face_cards:
    for suit in suits:
        if suit == 'Hearts':
            face_cards[face] = 'of Hearts'
           # print(face, face_cards[face])
            deck.append(f'{face} {face_cards[face]}')
        elif suit == 'Spades':
            face_cards[face] = 'of Spades'
           # print(face, face_cards[face])
            deck.append(f'{face} {face_cards[face]}')
        elif suit == 'Clubs':
            face_cards[face] = 'of Clubs'
           # print(face, face_cards[face])
            deck.append(f'{face} {face_cards[face]}')
        elif suit == 'Diamonds':
            face_cards[face] = 'of Diamonds'
            #print(face, face_cards[face])
            deck.append(f'{face} {face_cards[face]}')
#nested for loop to store all face cards

deck.sort()
#sort deck to print by suits

print("Here's the entire deck:")
for card in deck:
    print(card)
#loop through to print entire deck

print("Here are the Club cards:")
for card in range(0, 52, 4): 
    print(deck[card])
#loop through deck and print club cards