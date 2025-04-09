import json
#import json to load info in .json file created in favorite.py

filename = 'favorite_food.json'
#file definition


with open(filename) as f:
    food = json.load(f)
    print(f'I know your favorite food, its {food}!')
#open file and print statement accessing info in file

