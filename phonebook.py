phonebook = {'Nolan':'555-1111', 'Olivia': '555-2222', 'Abria': '555-3333', 'Nora': '555-4444'}
list = {'Nolan', 'Olivia', 'Ryan', 'Alex'}

print("These contacts are in the phonebook:")
for contact in phonebook:
     if contact in list:
        print(contact, phonebook[contact])
#for loop to check if contact in list is in phonebook
for name in list:
    if name not in phonebook :
        print(f"{name} is not in phonebook.")
#for loop to check if contact in list is not in phonebook