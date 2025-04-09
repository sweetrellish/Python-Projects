import json
#import json module to dump info into file

filename = 'favorite_food.json'
#file definition

food = input('What is your favorite food?\n')
#prompt to ask for favorite food

with open(filename, 'w') as f:
    json.dump(food, f)
#open file to write permission and dump info into file