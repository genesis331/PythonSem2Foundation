# Practical 1
# Q3

courseList = []
# Asks the user to input student ID, name, and courses taken
studentID = str(input("Please key in the student ID  : "))
studentName = str(input("Please enter student’s name : "))
courseCount = int(input("Number of courses registered: "))
course1 = str(input("Course 1: "))
courseList.append(course1)
course2 = str(input("Course 2: "))
courseList.append(course2)
course3 = str(input("Course 3: "))
courseList.append(course3)
course4 = str(input("Course 4: "))
courseList.append(course4)

# Prints the information
print("-"*60)
print("Student(id/name) : %s/%s" % (studentID, studentName))
print("-"*60)
print("Courses taken    : ", end="")
print(courseList[0], courseList[1], courseList[2], courseList[3], sep=", ")
