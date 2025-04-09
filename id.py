current_ids = ['Ryan', 'Bridget', 'Sam', 'Justin', 'Alex']
new_ids = ['Ryan', 'ALEX', 'Richard', 'Anna', 'Connor']
#initialize lists

for user in new_ids:
    if user not in current_ids and user == user.title():
        print(f"The username {user} is available.")
#for loop to check if new_id is in current list

for user in new_ids:
    for name in current_ids:
        if user.title() == name.title():
            user = user.title()
            print(f"The username {user} is taken, please select another username.")
#nested for loop to check for capitilization errors

#OLD CODE****
# elif user in new_ids != current_ids:
#     print(f"The username {user} is taken, \nplease select another username.")