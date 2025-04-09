heart_deck = [] #total card number list
count = 0 
card = 2
#initialize all variables

while count < 9:
    nameCard = f"{card} of Hearts"
    heart_deck.append(nameCard)
    card += 1
    count += 1
#while loop that adds card values to string list heart_deck

faceCards = ['Ace of Hearts', 'Jack of Hearts', 'Queen of Hearts', 'King of Hearts']
heart_deck.insert(0, faceCards[0])
heart_deck.insert(count+1, faceCards[1])
heart_deck.insert(count+2, faceCards[2])
heart_deck.insert(count+3, faceCards[3])
#set values of faceCards

print("Here's a list of all the Heart cards:")
for card in heart_deck[:]:
    print(card)
#for loop listing all values in heart_deck

print("\nHere's a list of number cards:")
for card in heart_deck[:10]:
    print(card)
#for loop printing number cards only

print("\nHere's all the face cards:")
for card in heart_deck[-3:]:
    print(card)
#for loop printing face cards

#OLD CODE*****
# print_count = 0
# while print_count < 13:
#     print(heart_deck[print_count])
#     print_count += 1
#use while loop to print all elements of heart deck

#OLD CODE*********
# print(faceCards[0])
# print2_count = 1
# while print2_count < 10:
#     print(heart_deck[print2_count])
#     print2_count += 1
# while loop printing only number cards and Ace

#OLD CODE********
# print3_count = 1
# while print3_count < 4:
#     print(faceCards[print3_count])
#     print3_count += 1
# while loop printing only face cards

