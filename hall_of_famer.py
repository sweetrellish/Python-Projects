def make_HOF(list, hof_list):
    """Adds Hall of Famer to each player in list"""
    for player in list:
        player = f'Hall of Famer {player}'
        hof_list.append(player)
#takes list and appends to new list hall of fame

def show_players(player_list):
    """Passes list to print players in list"""
    for player in player_list:
        print(player)
#prints list argument
    
players = ['Kobe Bryant', 'Shaq', 'Michael Jordan']
hof_players = []
make_HOF(players, hof_players)
show_players(hof_players)
#list definition and function call passing list through