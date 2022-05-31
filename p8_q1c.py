# Practical 8
# Q1c

record = {}
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
            # Appends the course code and grade to the dictionary
            record[courseCode] = grade
# Prints the dictionary
print('\nCourses taken:', record)
