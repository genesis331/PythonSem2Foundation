# Practical 8
# Q2

# From previous question
record = {}
while True:
    courseCode = input('\nCourse Code: ')
    if courseCode == 'Q':
        break
    else:
        grade = input('Grade: ')
        if grade == 'Q':
            break
        else:
            record[courseCode] = grade
print('\nCourses taken:', record)

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
