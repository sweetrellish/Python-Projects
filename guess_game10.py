print("Welcome to the Test Code\n\n")
name = "Pye"
prompt = "What is your name? \n"
prompt2 = "\nLet's play a game! I'm thinking of a number. \nPlease pick a number between 1-10, you have 3 tries. \n"
message =''
message2 = ''
correctNum = 5
count = 0

print("My name is ", name)

while message == '':				
	message = input(prompt)
	print("Nice to meet you", message)
while count < 3:
	message2 = input(prompt2)
	message2 = int(message2)
	if message2 != correctNum :
		count += 1
		if count < 3:
			print("Guess again")
	if message2 == correctNum:
		print("You guessed correct!")
		break
if message2 != correctNum:
	print("You didn't guess correctly \nPlease do better next time!")