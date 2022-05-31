# Final Assessment
# Q2 (DNF)

totalCreditHours = 0
totalGradePts = 0

gpaList = {
    "A+": 4.00,
    "A": 4.00,
    "A-": 3.67,
    "B+": 3.33,
    "B": 3.00,
    "B-": 2.67,
    "C+": 2.33,
    "C": 2.00,
    "F": 0.00
}

# Checks the grade based on the GPA list and returns the grade point
def checkGrade(marks):
    if marks >= 90:
        return "A+"
    elif marks >= 80:
        return "A"
    elif marks >= 75:
        return "A-"
    elif marks >= 70:
        return "B+"
    elif marks >= 65:
        return "B"
    elif marks >= 60:
        return "B-"
    elif marks >= 55:
        return "C+"
    elif marks >= 50:
        return "C"
    else:
        return "F"

# Asks the user to enter the name, student ID, CGPA target and course code
studName = input("Student Name >> ")
studId = input("Student ID >> ")
target = input("CGPA Target >> ")
courseCode = input("\nEnter Course Code <Q>uit >> ")
while courseCode != "Q":
    # Validates the course code
    if courseCode[:2] == "FH" and len(courseCode) == 8:
        # Asks the user to enter the description for the course
        courseDesc = input("Enter course description >> ")
        # Reads the credit hours from the course code entered
        creditHours = int(courseCode[-1])
        # Adds the credit hours to the total credit hours
        totalCreditHours += creditHours
        # Asks the user to enter the marks for the course
        courseMark = input("Enter course Marks >> ")
        courseGrade = checkGrade(int(courseMark))
        # Prints the grade attained for the course
        print("Grade attained: %s(%.2f)" % (courseGrade, gpaList[courseGrade]))
        # Adds the grade points to the total grade points
        totalGradePts += gpaList[courseGrade] * creditHours
    else:
        print("Error with course code entered")

    courseCode = input("\nEnter Course Code <Q>uit >> ")

# Print summary of the student
print("")
print("-" * 70)
print("Student Name (ID): %s(%s)\tCGPA Target: %.2f" % (studName, studId, float(target)))
print("-" * 70)
print("CGPA (total credit hours)\t\t: %.2f (%d)" % (totalGradePts / totalCreditHours, totalCreditHours))

# Determines the minimum grade to be achieved based on the CGPA target
for grade in gpaList:
    if gpaList[grade] > float(target):
        gradeBeforeTarget = grade
    else:
        break
print("Min grade for remaining courses to be taken: " + gradeBeforeTarget)
