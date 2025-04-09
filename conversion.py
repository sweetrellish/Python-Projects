prompt = "Please enter a starting and ending temperature: \n"
start = input(prompt)
end = input()
#initialize prompt and set input for start and end temp

start = int(start)
end = int(end)
#convert to integer

active = True
while active:
    farenheit = start * 9/5 + 32
    farenheit = int(farenheit)
    print(f"{start} degrees Celcius is {farenheit} Farenheit.")
    start += 1
    if start == end:
        print(f"{start} degrees Celcius is {farenheit} Farenheit.")
        active = False
#while loop using flag to loop through each temp from start to end
#and convert to Farenheit
