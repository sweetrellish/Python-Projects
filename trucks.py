trucks = ['Ford', 'Dodge', 'Chevy']
#initialize to include string values

print("I would like to own a", trucks[0], "truck.")
#recall first value in print statement
print("However I would also like to own a", trucks[1], "or", trucks[2], "truck as well.")
#implement other values in print statement

trucks.append('Toyota')
#add Toyota to the end of the list
print(trucks)
#verify by printing list
trucks.insert(1, 'GMC')
#add GMC to postion 1 in list
print(trucks)

num = len(trucks)
#set list length to num
print("There are", num, 'trucks in my list.')

print(trucks)
print(sorted(trucks))
#temporarily sort alphabetically
print(trucks)

trucks.sort()
#permanently sort alphabetically
print(trucks)
trucks.reverse()
#reverse the order of the list
print(trucks)

del trucks[0]
#delete Toyota from first position
popped_truck = trucks.pop(0)
#set variable equal to GMC, position 0 in list now
print(trucks)

print("I already owned a ", popped_truck, 'truck.')
#print statement using variable

trucks.remove('Chevy')
#remove Chevy from the list
print(trucks)






