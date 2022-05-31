# Practical 1
# Q2

# Asks for number of wheels, price, license type and registration number
wheelsNum = int(input("Please key in the number of wheels : "))
price = float(input("Please key in the price            : "))
licenseType = str(input("Please key in the license type     : "))
regNo = str(input("Please key in the registration no. : "))

# Prints the information
print("This vehicle has %d wheels. The price is RM %.2f." % (wheelsNum, price))
print("You are to have a Type %s driving license." % licenseType)
print("The registration no. of this vehicle is %s." % regNo)
