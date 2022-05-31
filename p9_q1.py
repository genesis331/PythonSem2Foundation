# Practical 9
# Q1

record = []
cgpaPts = {
    'A+': 4.000,
    'A': 4.000,
    'A-': 3.667,
    'B+': 3.333,
    'B': 3.000,
    'B-': 2.667,
    'C+': 2.333,
    'C': 2.000,
    'F': 0.000
}
totalGradePts = 0
totalCreditHrs = 0

# Opens studCGPA.txt and allows append-only access
with open("studCGPA.txt", "a") as f:
    while True:
        # Asks for the course code
        courseCode = input('\nCourse Code: ')
        # Checks if the user wants to quit
        if courseCode == 'Q':
            # Breaks the loop
            break
        else:
            # Writes the course code to the file
            f.write('\nCourse Code: ' + courseCode + "\n")
            # Asks for the grade
            grade = input('Grade: ')
            # Checks if the user wants to quit
            if grade == 'Q':
                # Breaks the loop
                break
            else:
                # Appends the course code and grade to the list
                record.append([courseCode, grade])
                # Writes the grade to the file
                f.write('Grade: ' + grade + "\n")

    for i in range(len(record)):
        # Extracts the credit hours from course code
        creditHrs = int(record[i][0][-1])
        # Adds the credit hours to the total credit hours
        totalCreditHrs += creditHrs
        # Adds grade points to the total grade points
        totalGradePts += cgpaPts[record[i][1]] * creditHrs
        # Calculates total CGPA
        totalCGPA = totalGradePts / totalCreditHrs

    # Prints the total CGPA
    print('\nCGPA: %.3f' % totalCGPA)
    # Writes the total CGPA to the file
    f.write('\nCGPA: %.3f' % totalCGPA)
