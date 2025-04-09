my_classes = ['CMP135', 'MTH121', 'ENG101', 'BIO101']
friends_classes = my_classes[:]
#initialize my_classes and copy list to friends_classes

my_classes.append('CMP141')
friends_classes.append('CMP115')
#add different classes to each list

print("My classes are:")
for classes in my_classes:
    print(classes)
#print my classes

print("My friend's classes are:")
for classes in friends_classes:
    print(classes)
#print friends classes