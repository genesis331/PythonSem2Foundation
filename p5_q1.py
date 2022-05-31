# Practical 5
# Q1

currentInput = 0
# Checks if the input is not greater or equal to 0
while currentInput <= 999:
    # Asks for the temperature
    inputTempinF = float(input("Enter the temperature in Fahrenheit: "))
    currentInput = inputTempinF
    if currentInput <= 999: 
        # Converts the temperature to Celsius then prints the result
        tempinC = (inputTempinF - 32) * 5/9
        print("The temperature in Celsius is: %.2f" % tempinC)
    else:
        # Prints a goodbye message
        print("End of Program")
