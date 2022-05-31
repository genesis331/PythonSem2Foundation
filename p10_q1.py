# Practical 10
# Q1

studentList = []
toContinue = True
# Opens studentsprofile.txt and allows append-only access
with open ("studentsprofile.txt", "a") as f: 
    while toContinue:
        # Asks for the student's first name, last name, student ID, age and country
        firstName = input("First name: ")
        lastName = input("Last name: ")
        studentID = input("Student ID: ")
        age = input("Age: ")
        country = input("Country: ")
        # Appends the student's information to the list
        studentList.append([firstName, lastName, studentID, age, country])
        # Writes the student's information to the file
        f.write(firstName + "," + lastName + "," + studentID + "," + age + "," + country)
        # Asks if the user wants to continue
        toContinuePrompt = input("Do you want to continue? (y/n): ")
        print("")
        if toContinuePrompt == 'n':
            toContinue = False
        else:
            # Writes a new line to the file
            f.write("\n")

# Asks if the user wants to see a preview of the list
toPreviewPrompt = input("Do you want to preview? (y/n): ")
# Asks for a search string
searchString = input("Enter search string >> ")

# Prints information based on the user's search string
print("\nName\t\t\tStudent ID\tAge\tCountry")
print("-"*60)
for i in range(len(studentList)):
    if studentList[i][0] == searchString or studentList[i][1] == searchString or studentList[i][2] == searchString or studentList[i][3] == searchString or studentList[i][4] == searchString:
        print(studentList[i][0] + " " + studentList[i][1] + "\t\t" + studentList[i][2] + "\t\t" + studentList[i][3] + "\t" + studentList[i][4])
