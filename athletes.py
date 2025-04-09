michael_jordan ={'Name': 'Michael Jordan', 'Sport': 'Basketball', 'Team': 'Chicago Bulls', 'Number': '23', 'Position': 'Shooting Guard\n'}
kobe_bryant = {'Name': 'Kobe Bryant', 'Sport': 'Basketball', 'Team': 'L.A. Lakers', 'Number': '24', 'Position': 'Small Forward\n'}
peyton_manning = {'Name': 'Peyton Manning', 'Sport': 'Football', 'Team': 'Indianapolis Colts', 'Number': '18', 'Position': 'Quarterback\n'}
#create athlete dictionaries

athletes = []
athletes.append(michael_jordan)
athletes.append(kobe_bryant)
athletes.append(peyton_manning)
#add athletes to list

for athlete in athletes:
    for info in athlete:
        print(f'{info}:{athlete[info]}')
#loop through list and print info of each athlete