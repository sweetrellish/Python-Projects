from operator import truediv


prompt = "Enter your favorite ice cream flavors "
prompt += "and enter 'quit' when finished : "
flavor = ''
#initialize prompts and input variable

while flavor != 'quit':
    flavor = input(prompt)
    if flavor != 'quit':
        print(f"I will add {flavor} to your sundae.")
#while loop using conditional statement

active = True
while active:
    flavor= input(prompt)
    if flavor == 'quit':
        active = False
    else:
        print(f"I will add {flavor} to your sundae.")
#while loop using flag variable

while True:
    flavor = input(prompt)
    if flavor == 'quit':
        break
    else:
        print(f"I will add {flavor} to your sundae.")
#while loop using break statement