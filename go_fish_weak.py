#DEBUG NOTES
#may incur index error when looping through when move == 2 or at start of program, doesn't occur in every instance of execution, exit terminal and start again 


import random
import deck_functions
import card_functions
import json
                    
cardValues = {"A": 11,"2": 2,"3": 3,"4": 4,"5": 5,"6": 6,"7": 7,"8": 8,"9": 9,"10": 10,"J": 10,"Q": 10,"K": 10}
filename = 'go_fish.json'
uturn = 0
cturn = 0
uwin = 0
cwin = 0
image = []
cimage = []
table = {}
table_image = f'\tTABLE\n-------------------------\n|{image}\t\t\n-------------------------\n'
deck = card_functions.build_deck()
deck_functions.shuffle_deck(deck)
#create deck and shuffle

print("\t~Welcome to Go-Fish!~\n-----Here is your starting hand-----")
user = deck_functions.deal_hand(deck, 7)
print(user)
#start screen and starting hand

comp = deck_functions.deal_hand(deck, 7)
print(f'Computer:{comp}')
#init computer hand

ccount = 1              #computer dictionary index
count = 1               #dictionary table counter
while True:             #game loop
    pair =[]                        #pair list
    comp_pair = []                  #computer pair list
    clones = user.copy()            #clone hand to check pairs
    comp_clones = comp.copy()       #computer clone hand

    table = {}                      #table dictionary to store played pairs
    comp_table = {}

    menu = "-----Action Menu-----\n1)\tDraw a card \n2)\tPlay a pair\n3)\tAsk for a card\n4)\tQuit"     #action menu interface
    prompt = input(f'{menu}\nEnter your selection: ')                                                   #prompt for player
    prompt = int(prompt)

    if prompt == 1:
        user.append(deck_functions.deal_top_card(deck))                                                 #draws the top card into the hand
        print(f'\tHAND\n{user}')
        print(f'\tCOMPUTER HAND\n{comp}') 
        uturn += 1    

    elif prompt == 2:
        pair = deck_functions.hand_pairs(user, clones)                                                  #checks for pairs
        if pair:
            for pairs in pair:
                image.append(pairs) 
                table[f'Pair {count}'] = pairs                     #if pair exists, loop through to add each pair to table
            pair.remove(pairs)                                                                          #remove pair list
            table_image = f'\tTABLE\n-------------------------\n|{image}\t\t\n-------------------------\n'
            count += 1
            print(table_image)
            print(f'\tHAND\n{user}')
            print(f'\tCOMPUTER HAND\n{comp}')
            uturn += 1
            continue

    elif prompt == 3:
       fish = input('What card would you like?\n')
       flag = 0
    #    try:
       for chand in comp:
            if card_functions.same_Value(fish, chand):  
                image.append(chand)                                                    #fish for cards in computers hand
                user.append(chand)                                                #if card is in computers hand (has same value), adds card to hand
                clones.append(chand)
                table[f'Pair {count}'] = chand
                comp.remove(chand)                                                  #takes card from computers hand, could be made to method()
                # comp.remove(chand)                                                #adds to user hand and clone, adds pair to table, removes from computer hand
                
                pair = deck_functions.hand_pairs(user, clones)                           #checks for pairs and prints hands
                if pair:
                    for i, pairs in enumerate(pair):
                        image.append(pairs) 
                        table[f'Pair {count}'] = pairs                     #if pair exists, loop through to add each pair to table
                    pair.remove(pairs)                                                                          #remove pair list
                    table_image = f'\tTABLE\n-------------------------\n|{image}\t\t\n-------------------------\n'
                    count += 1
                print(table_image)
                print(f'\tHAND\n{user}')
                print(f'\tCOMPUTER HAND\n{comp}')
                flag += 1
                count += 1
                uturn += 1
       
       if flag == 0:                                                                 #if no pairs found, print go-fish
            print('Go-Fish!')
            print('Drawing a card...')
            user.append(deck_functions.deal_top_card(deck))
            print(f'\tHAND\n{user}')
            print(f'\tCOMPUTER HAND\n{comp}')
            uturn += 1
    #    except ValueError:
    #         print('Card not in hand...')                                                  #exception block for error message

    elif prompt == 4:                             #loop exit conditions
        break
    elif deck_functions.empty_hand(user):
        break
    elif deck_functions.empty_hand(deck):
        break
    elif deck_functions.empty_hand(comp):
        break
        

    computer_turn = True
    while computer_turn:

        print("Computer turn...")
        comp_pair = deck_functions.hand_pairs(comp, comp_clones)
        if comp_pair:
            for cpairs in comp_pair:
                cimage.append(cpairs)
                comp_table[f'Pair {ccount}'] = cpairs                       #if pair exists, loop through to add each pair to computer table
            comp_pair.remove(cpairs)
            ccount += 1
            print(f'Computer played: {cpairs}')
            ctable_image = f'\tCOMPUTER TABLE\n-------------------------\n|{cimage}\t\t\n-------------------------\n'
            print(ctable_image)


        # elif fish in comp:
        #     user_ans = input(f'Do you have a {fish}? y/n\n')
        #     try:
        #         if user_ans == 'y':             
        #             for fishes in user:
        #                 if card_functions.same_Value(user, fishes):            
        #                     cimage.append(fishes)
        #                     comp.append(fishes)                                  #if card is in computers hand (has same value), adds card to hand
        #                     comp_clones.append(fishes)
        #                     comp_table[f'Pair {ccount}'] = fishes               #takes card from computers hand, could be made to method()
        #                     user.remove(fishes)                                  #adds to user hand and clone, adds pair to table, removes from computer hand
        #                     deck_functions.hand_pairs(comp, comp_clones)         #checks for pairs and prints hands
        #                     ccount += 1
        #                     cturn += 1
        #                     computer_turn = False

        #         elif user_ans == 'n':
        #             print('Go-Fish!')
        #             comp.append(deck_functions.deal_top_card(deck))
        #             print(f'\tHAND\n{user}')
        #             print(f'\tCOMPUTER HAND\n{comp}')
        #             cturn += 1
        #             computer_turn = False

        #     except ValueError:
        #         pass

        if comp:
            choice = deck_functions.hand_random_card(comp)
            user_ans = input(f'Do you have a {choice}? y/n\n')

            try:
                if user_ans == 'y':             
                    for fishes in user:
                        if card_functions.same_Value(user, fishes):            
                            cimage.append(fishes)
                            comp.append(fishes)                                                #if card is in computers hand (has same value), adds card to hand
                            comp_clones.append(fishes)
                            comp_table[f'Pair {ccount}'] = fishes                              #takes card from computers hand, could be made to method()
                            user.remove(fishes)                                                #adds to user hand and clone, adds pair to table, removes from computer hand
                            deck_functions.hand_pairs(comp, comp_clones)                       #checks for pairs and prints hands
                            ccount += 1
                            cturn += 1
                            computer_turn = False

                elif user_ans == 'n':
                    print('Go-Fish!')
                    comp.append(deck_functions.deal_top_card(deck))
                    print(f'\tHAND\n{user}')
                    print(f'\tCOMPUTER HAND\n{comp}')
                    cturn += 1
                    computer_turn = False

            except ValueError:
                pass

        else:
            comp.append(deck_functions.deal_top_card(deck))
            print(f'\tHAND\n{user}')
            print(f'\tCOMPUTER HAND\n{comp}')
            cturn += 1
            computer_turn = False

    if deck_functions.empty_hand(user):
        break
    elif deck_functions.empty_hand(deck):
        break
    elif deck_functions.empty_hand(comp):
        break
if count > ccount:
    print('You won!...\nThanks for playing!')
    uwin += 1
else:
    print('You lost!...\nPlease try again!')
    cwin += 1

# with open(filename, 'a') as f:
#     f.write(f'USER WINS: {uwin}\nCOMPUTER WINS: {cwin} \nUSER TURNS: {uturn}\nCOMPUTER TURNS: {cturn}\nUSER PAIRS: {count}\nCOMPUTER PAIRS: {ccount}')
file = f'USER WINS: {uwin} COMPUTER WINS: {cwin} USER TURNS: {uturn} COMPUTER TURNS: {cturn}'
with open(filename, 'w')as f:
    json.dump(file, f)

for key in table:
    print(key)

    


#OLD CODE 4/13/2022

# for cards in user:                      #nested for loop to check value and ensure true pair, could act as method for handPairs(), adds to pair list and removes from hand
#     for clone in clones:                
#         if card_functions.get_Value(cards) == card_functions.get_Value(clone) and card_functions.get_suit(cards) != card_functions.get_suit(clone):
#             pair.append(cards)
#             pair.append(clone)
#             user.remove(cards)
#             user.remove(clone)
#             print(f"Storing {cards, clone} into pairs...")

# if pair:
#     print(f'Pairs: {pair}\n')
# else:
#     print('You have no pairs.\n')


# print("\n-----Here is the Computer's hand-----")
# comp = deck_functions.deal_hand(deck, 7)
# print(comp)

# print("\nSearching for pairs now...")
# clone = user.copy()
# user.sort()

# pair = []

# for num in range(7):
#     if card_functions.get_Value(user[num]) in clone[num]:
#         pair.append(user[num])

# if pair:
#     print(f'You have a pair of {pair}')
# else:
#     print('You have no pairs.')

# while uwin == 0 or cwin == 0:
#     menu = "-----Action Menu-----\n1)\tDraw a card \n2)\tPlay a pair\n3)\tAsk for a card\n4)\tGo-Fish!"
#     prompt = input(f'{menu}\nEnter your selection: ')
#     prompt = int(prompt)
#     if prompt == 1:
#         new_card = deck_functions.deal_top_card(deck)
#         user.append(new_card)
#     elif prompt == 2:
#         for card in pair:
#             table = pair.pop(card)
#             user.pop(card)
#             print(f'You have played {table[card]}')
#     elif prompt == 3:
#         query = input("What card do you want to ask for?\nEnter the exact card:")
#         print(f'Do you have a {query}?')
#         for card in comp:
#             if query in card:
#                 ccard = comp.pop(f'{card}')
#                 user.append(ccard)
#     elif prompt == 4:
#         print('Go-Fish!')
        
#     if user == None:
#         uwin += 1
#     elif comp == None:
#         cwin += 1

        

