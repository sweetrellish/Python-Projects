prompt = "Please enter your height in inches:\n"
height = input(prompt)
height = int(height)
#initialize all variables and prompt for height input
#set height as int so it can be printed in f string

if height <= 40:
    print(f"You are {height} inches tall,")
    print("There are 20 rides you can ride.")
elif height > 40 and height <= 42 :
    print(f"You are {height} inches tall,")
    print("There are 28 rides you can ride.")
elif height > 42 and height <= 48 :
    print(f"You are {height} inches tall,")
    print("There are 35 rides you can ride.")
elif height > 48 and height <= 53 :
    print(f"You are {height} inches tall,")
    print("There are 36 rides that you can ride.")
elif height > 53 :
    print(f"You are {height} inches tall,")
    print("You may ride all the rides.")
#if-elif-else loop block to evaluate heaight and check to see what rides they can ride