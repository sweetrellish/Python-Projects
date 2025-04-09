heart = []
count = 2
#initialize list and counter for loop

while count < 11:
    heart.insert(count, f'{count} of Hearts')
    count += 1
#loop to insert card number values into list

print(heart[0])
print(heart[1])
print(heart[2])
#print 3 values in list of cards