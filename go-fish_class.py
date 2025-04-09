from Deck_classes import Deck

deck = Deck()
deck.shuffle_deck()

user = deck.deal_hand(7)
comp = deck.deal_hand(7)
uturn = 0
cturn = 0
uwin = 0
cwin = 0
image = []
cimage = []
table = {}
table_image = f'\tTABLE\n-------------------------\n|{image}\t\t\n-------------------------\n'

print(f"Welcome to Go-Fish\nHere is your starting hand:  {user}")
ccount = 1              #computer dictionary index
count = 1               #dictionary table counter

while True:
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
        user.append(deck.deal_top_card(deck))                                                 #draws the top card into the hand
        print(f'\tHAND\n{user}')
        print(f'\tCOMPUTER HAND\n{comp}') 
        uturn += 1    

    elif prompt == 2:
        pair = deck.hand_pairs(user, clones)                                                  #checks for pairs
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
            if deck.same_Value(fish, chand):  
                image.append(chand)                                                    #fish for cards in computers hand
                user.append(chand)                                                #if card is in computers hand (has same value), adds card to hand
                clones.append(chand)
                table[f'Pair {count}'] = chand
                comp.remove(chand)                                                  #takes card from computers hand, could be made to method()
                                                                              #adds to user hand and clone, adds pair to table, removes from computer hand
                
                pair = deck.hand_pairs(user, clones)                           #checks for pairs and prints hands
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
                flag += 1
                count += 1
                uturn += 1
       
       if flag == 0:                                                                 #if no pairs found, print go-fish
            print('Go-Fish!')
            print('Drawing a card...')
            user.append(deck.deal_top_card(deck))
            print(f'\tHAND\n{user}')
            print(f'\tCOMPUTER HAND\n{comp}')
            uturn += 1
    #    except ValueError:
    #         print('Card not in hand...')                                                  #exception block for error message

    elif prompt == 4:                             #loop exit conditions
        break
    elif deck.empty_hand(user):
        break
    elif deck.empty_hand(deck):
        break
    elif deck.empty_hand(comp):
        break
        

    computer_turn = True
    while computer_turn:

        print("Computer turn...")
        comp_pair = deck.hand_pairs(comp, comp_clones)
        if comp_pair:
            for cpairs in comp_pair:
                cimage.append(cpairs)
                comp_table[f'Pair {ccount}'] = cpairs                       #if pair exists, loop through to add each pair to computer table
            comp_pair.remove(cpairs)
            ccount += 1
            print(f'Computer played: {cpairs}')
            ctable_image = f'\tCOMPUTER TABLE\n-------------------------\n|{cimage}\t\t\n-------------------------\n'
            print(ctable_image)


        elif fish in comp:
            user_ans = input(f'Do you have a {fish}? y/n\n')
            try:
                if user_ans == 'y':             
                    for fishes in user:
                        if deck.same_Value(user, fishes):            
                            cimage.append(fishes)
                            comp.append(fishes)                                  #if card is in computers hand (has same value), adds card to hand
                            comp_clones.append(fishes)
                            comp_table[f'Pair {ccount}'] = fishes               #takes card from computers hand, could be made to method()
                            user.remove(fishes)                                  #adds to user hand and clone, adds pair to table, removes from computer hand
                            deck.hand_pairs(comp, comp_clones)         #checks for pairs and prints hands
                            ccount += 1
                            cturn += 1
                            computer_turn = False

                elif user_ans == 'n':
                    print('Go-Fish!')
                    comp.append(deck.get_random_card(deck))
                    print(f'\tHAND\n{user}')
                    print(f'\tCOMPUTER HAND\n{comp}')
                    cturn += 1
                    computer_turn = False

            except ValueError:
                pass

        elif comp:
            choice = deck.hand_random_card(comp)
            user_ans = input(f'Do you have a {choice}? y/n\n')

            try:
                if user_ans == 'y':             
                    for fishes in user:
                        if deck.same_Value(user, fishes):            
                            cimage.append(fishes)
                            comp.append(fishes)                                                #if card is in computers hand (has same value), adds card to hand
                            comp_clones.append(fishes)
                            comp_table[f'Pair {ccount}'] = fishes                              #takes card from computers hand, could be made to method()
                            user.remove(fishes)                                                #adds to user hand and clone, adds pair to table, removes from computer hand
                            deck.hand_pairs(comp, comp_clones)                       #checks for pairs and prints hands
                            ccount += 1
                            cturn += 1
                            computer_turn = False

                elif user_ans == 'n':
                    print('Go-Fish!')
                    comp.append(deck.get_random_card(deck))
                    print(f'\tHAND\n{user}')
                    print(f'\tCOMPUTER HAND\n{comp}')
                    cturn += 1
                    computer_turn = False

            except ValueError:
                pass

        else:
            comp.append(deck.get_random_card(deck))
            print(f'\tHAND\n{user}')
            print(f'\tCOMPUTER HAND\n{comp}')
            cturn += 1
            computer_turn = False

    if deck.empty_hand(user):
        break
    elif deck.empty_hand(deck):
        break
    elif deck.empty_hand(comp):
        break
if count > ccount:
    print('You won!...\nThanks for playing!')
    uwin += 1
else:
    print('You lost!...\nPlease try again!')
    cwin += 1