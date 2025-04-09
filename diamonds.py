diamond_deck = [] #total card number list
count = 0 
card = 2
#initialize all variables

while count < 9:
    nameCard = f"{card} of Diamonds"
    diamond_deck.append(nameCard)
    card += 1
    count += 1
#while loop that adds card values to string list heart_deck

faceCards = ['Ace of Diamonds', 'Jack of Diamonds', 'Queen of Diamonds', 'King of Diamonds']
diamond_deck.insert(0, faceCards[0])
diamond_deck.insert(count+1, faceCards[1])
diamond_deck.insert(count+2, faceCards[2])
diamond_deck.insert(count+3, faceCards[3])

# print("Here's a list of all the Diamond cards:")
# print_count = 0
# while print_count < 13:
#     print(diamond_deck[print_count])
#     print_count += 1
# #use while loop to print all elements of diamond deck

#UNUSED CODE FROM HEARTS.PY
# print("\nHere's a list of number cards:")
# print2_count = 1
# while print2_count < 10:
#     print(diamond_deck[print2_count])
#     print2_count += 1
# # while loop printing only number cards

# print("\nHere's all the face cards:")
# print3_count = 1
# while print3_count < 4:
#     print(faceCards[print3_count])
#     print3_count += 1
# # while loop printing only face cards
