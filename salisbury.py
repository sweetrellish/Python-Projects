
with open('Salisbury.txt') as file_object:
    lines = file_object.read()
    print(lines)
    #open file and read in entire file and print contents

with open('Salisbury.txt') as file_object:
    for line in file_object:
        print(line.rstrip())
    #open file and loop over file object to print contents

with open('Salisbury.txt') as file_object:
        line_list = file_object.readlines()
        for line in line_list:
            print(line.rstrip())
    #open file and read in contents to a list and print every item in list