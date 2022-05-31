# Practical 5
# Q2

twentyFourHourFormatInput = 0
amOrPm = "AM"
# Checks if the input is not equal or greater than 9999
while int(twentyFourHourFormatInput) < 9999:
    # Asks for the time
    twentyFourHourFormatInput = input("Enter the time in 24-hour format: ")
    if int(twentyFourHourFormatInput) < 9999:
        # Extracts the hour and the minute
        hour = twentyFourHourFormatInput[0:2]
        minute = twentyFourHourFormatInput[2:4]
        # Validaes the time
        if (int(hour) >= 0 and int(hour) <= 23 and int(minute) >= 0 and int(minute) <= 59):
            # Converts the time to 12-hour format
            if int(hour) > 12:
                hour = int(hour) - 12
                amOrPm = "PM"
            elif int(hour) == 0:
                hour = 12
            elif int(hour) == 12:
                amOrPm = "PM"
            # Prints the time in 12-hour format
            print("The time in 12-hour format: %s:%s %s" % (hour, minute, amOrPm))
        else:
            # Prints an error message
            print("The input is invalid")
    else:
        # Prints a divider line
        print("-------------------------------------------")
