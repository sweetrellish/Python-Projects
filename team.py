team = ['olivia', 'sam', 'lexi', 'grace', 'allison']
#initialize team
print("Here's a list of my team: ")
for value in team:
    print(value.title())
#print all team values
print("Here are the first three players: ")
for player in team[:3]:
    print(player.title())
#print first 3 players
print("Here are the middle players: ")
for player in team[1:4]:
    print(player.title())
#print middle players
print("Here are the last three players: ")
for player in team[-3:]:
    print(player.title())
#print last 3 players
