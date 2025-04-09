import card_functions
import deck_functions
import json

filename = 'blackjack.json'

deck = card_functions.build_deck()
deck_functions.shuffle_deck(deck)               #build deck

user = deck_functions.deal_hand(deck, 2)        # deal hands
house = deck_functions.deal_hand(deck, 2)

                                             #initialize variables for counting and ace value, totals
ace = ''
total = 0
total1 = 0
uwin = 0
cwin = 0
uturn = 0
cturn = 0

print('Welcome to BlackJack')                   #start menu and set value for aces
ace = input('Are aces high or low?\n')

while True:
    print(f'Your Hand: {user}')                     #print starting hand and action menu
    print(f'House hand: {house}')
    print('ACTION MENU\n\n1)Hit me\n2)Stay\n3)Fold')
    move = input('Selection :')                         #takes user input and checks value for face cards in house hand
    move = int(move)
   
    if move == 1:
        user.append(deck_functions.get_random_card(deck))         #draws card, checks value of face cards in hand, prints hand
        # print(f'Your hand: {user}')
        total = deck_functions.hand_Value(user, ace)
        total1 = deck_functions.hand_Value(house, ace)

        if total > 21:                                    #if total is greater than 21 you lose
            print(f'House: {house}')
            print(f'Your hand: {user}')
            print('Bust!')
            cwin += 1
            break
        elif total1 == 21 and total < 21:                               #if house has 21 they win automatically
            print(f'House: {house}')
            print(f'Your hand: {user}')
            print('The house wins!')
            cwin += 1
            break
        else:
            uturn += 1
            continue
    elif move == 2:                                             #player keeps hand, house draws 
        print('House draws a card...')
        house.append(deck_functions.get_random_card(deck))
        cturn += 1
        total1 = deck_functions.hand_Value(house, ace)
        total = deck_functions.hand_Value(user, ace)
           
        if total > 21:                                       #if total is greater than 21 you lose
            print(f'Your hand: {user}')
            print('Bust!')
            cwin += 1
            break
        elif total == 21 and total1 != 21:             #if total is 21 and house doesn't equal 21 you win
            print(f'Your hand: {user}')
            print('You win!')
            uwin += 1
            break
        elif total1 == 21 and total != 21:             #if total is not 21 and house has 21 you lose
            print(f'Your hand: {user}')
            print(f'House: {house}')
            print('The house wins!')
            cwin += 1
            break
        elif total1 > 21:
            print(f'Your hand: {user}')
            print(f'House: {house}')
            print('You win!')
            uwin += 21
            break
        
    elif move == 3:                                                 #exit loop user input
        print(f'House: {house}')
        print('The house wins!')
        print('Thanks for playing, please try again!')
        cwin += 1
        break

file = f'USER WINS: {uwin} COMPUTER WINS: {cwin} USER TURNS: {uturn} COMPUTER TURNS: {cturn}'
with open(filename, 'w')as f:
    json.dump(file, f)