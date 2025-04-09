filename = 'games.txt'
count = 0
#file definition

with open(filename, 'w') as file_object:
    while True:
        prompt = "Enter your favorite game(enter quit to exit):\n"
        game = input(prompt)
        
        if game == 'quit':
            break
        print(f"{game} is one of your favorite games.")
        file_object.write(f"{game}\n")
    #loop that while file is opened, prompt appends user's favorite game to file
