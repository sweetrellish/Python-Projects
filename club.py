computer_club = ['andy', 'greg', 'michael j.', 'fox', 'ADMIN']
#computer_club = ['']
#comment code to switch to empty list

for user in computer_club:
    if user.title() == 'Admin':
        print("Welcome Administrator!")
    elif user == '':
        print("Seek out more members!")
    else:
        print(f"Welcome to the club, {user.title()}!")
#for loop to check club members and print special message for admin