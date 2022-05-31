# Practical 8
# Q1b

record = []
while True:
    # Asks for the course code
    courseCode = input('\nCourse Code: ')
    # Checks if the user wants to quit
    if courseCode == 'Q':
        # Breaks the loop
        break
    else:
        # Asks for the grade
        grade = input('Grade: ')
        # Checks if the user wants to quit
        if grade == 'Q':
            # Breaks the loop
            break
        else:
            # Appends the course code and grade to the list
            record.append((courseCode, grade))
# Converts the list to a tuple
recordInTuple = tuple(record)
# Prints the tuple
print('\nCourses taken:', recordInTuple)
