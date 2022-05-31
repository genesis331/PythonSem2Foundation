# Practical 4
# Q1

# Asks for the retail price and transaction code
retailPrice = float(input("Retail price: "))
transactionCode = str(input("Transaction code: "))

errStatus = False
# Checks the transaction code and calculates the commission
if transactionCode == "S":
    commision = 0.05 * retailPrice
elif transactionCode == "M":
    commision = 0.07 * retailPrice
elif transactionCode == "L":
    commision = 0.10 * retailPrice
else:
    # Prints warning message
    print("Invalid transaction code")
    errStatus = True

# Checks if there is an error
if not errStatus:
    # Prints a summary
    employeeNum = str(input("Employee number: "))
    print("\nOUTPUT")
    print("---------------------------------------------")
    print("Retail price : %.2f" % retailPrice)
    print("Commission : %.2f" % commision)
    print("Employee number : %s" % employeeNum)
    print("---------------------------------------------")
