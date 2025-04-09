program_requests = ['athletes.py', 'class.py', 'course.py', 'full_deck.py', 'phonebook.py']
finished_programs = []
#initialize lists

while program_requests:
    current_program = program_requests.pop()
    print(f"I made your program {current_program}")
    finished_programs.append(current_program)
#while loop moving each instance of program_requests to finished_programs

for program in finished_programs:
    print(f"I have completed the {program} program.")
#for loop printing through each value in finished_programs