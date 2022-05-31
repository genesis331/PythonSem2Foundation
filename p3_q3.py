# Practical 3
# Q3

# Asks for the age
age = int(input("Enter age: "))
# Checks if the age is more or equal to 3
if age >= 3:
    # Checks if the age is more or equal to 13
    if age >= 13:
        # Checks if the age is more than 55
        if age > 55:
            print("RM7")
        else:
            print("RM10")
    else:
        print("RM5")
else:
    print("Free")
