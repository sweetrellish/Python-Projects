filename = 'Breakfast.txt'
filename2 = 'Dinner.txt'
#file definition

try:
    with open(filename, encoding = 'utf-8') as f:
        content = f.read()
        print(content)
except FileNotFoundError:
    print(f'Sorry, the file {filename} does not exist.')
#try except block to cover FileNotFound error, opens file and prints contents

try:
    with open(filename2, encoding= 'utf-8') as f:
        content2 = f.read()
        print(content2)
except FileNotFoundError:
    print(f'Sorry, the file {filename2} does not exist.')
#try except block to cover FileNotFound error, opens file and prints contents
