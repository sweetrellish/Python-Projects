with open('Salisbury.txt') as file_object:

    for line in file_object:
        line = line.replace('Salisbury', 'Berlin')
        print(line.rstrip())
    #open file and use replace function to sub Berlin in for Salisbury