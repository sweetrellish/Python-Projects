prompt = 'Please enter a number : '
#initialize prompt variable

response = input(prompt)
response = int(response)
#input user response and convert to integer

if response % 5 == 0:
    print("That number was a multiple of 5!")
else:
    print("That number was not a multiple of 5.")
#checks if input is multiple of 5