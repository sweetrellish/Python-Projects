course_log = {'intro to programming': 'web development', 'calculus': 'mathematics', 'differential equations': 'mathematics'}
#create dictionary of classes and majors

for course in course_log:
    print(f"{course.title()} is a class\nin the major of {course_log[course].title()}\n")
#print classes and majors from dict.

print("Here are the classes:")
for subject in course_log:
    print(subject.title())
#print only the classes

print("Here are the majors:")
for major in course_log:
    print(course_log[major].title())
#print only the majors