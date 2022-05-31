# Test 2
# Q3

vaccinationTrue = 0

# Limits the number of students that can enter their vaccination status (150)
for i in range(1, 151):
    print("Student %d:" % i)
    # Asks the user if they have been fully vaccinated
    vaccinationStatus = input("Have you received full vaccination? (yes/no): ")
    if vaccinationStatus == "yes":
        loopStatus = True
        # Loops until the user enters a valid date
        while loopStatus == True:
            # Asks the user for the date of vaccination
            vaccinationDate = input("Enter the date you received the full vaccination (dd/mm): ")
            # Checks if the month is between 1 and 12 (valid month)
            if int(vaccinationDate[3:5]) >= 1 and int(vaccinationDate[3:5]) <= 12:
                # Checks if the month has only 30 days
                if (int(vaccinationDate[3:5]) in (2, 4, 6, 9, 11)):
                    # Checks if the day is between 1 and 30 (valid day)
                    if int(vaccinationDate[0:2]) >= 1 and int(vaccinationDate[0:2]) <= 30:
                        vaccinationTrue += 1
                        loopStatus = False
                    else:
                        print("Invalid day!")
                else:
                    # Checks if the day is between 1 and 31 (valid day)
                    if int(vaccinationDate[0:2]) >= 1 and int(vaccinationDate[0:2]) <= 31:
                        vaccinationTrue += 1
                        loopStatus = False
                    else:
                        print("Invalid day!")
            else:
                print("Invalid month!")
    print("")

# Print summary of vaccination status
print("Total students who have been fully vaccinated: %d" % vaccinationTrue)
print("Total students who have not been fully vaccinated: %d" % (150 - vaccinationTrue))
