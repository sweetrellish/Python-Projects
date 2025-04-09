favorite_activities = ['drawing', 'lifting', 'gaming']
nfavorite_activity1 = 'cleaning'
nfavorite_activity2 = 'running'
#initialize all lists and not favorite activities

if 'drawing' in favorite_activities:
    print("Drawing is one of my favorite activies.")
if 'lifting' in favorite_activities:
    print("Lifting is one of my favorite activies.")
if 'gaming' in favorite_activities:
    print("Gaming is one of my favorite activies.")
if nfavorite_activity1 not in favorite_activities:
    print(f"{nfavorite_activity1.title()} isn't a favorite.") 
if nfavorite_activity2 not in favorite_activities:
    print(f"{nfavorite_activity2.title()} isn't a favorite.")