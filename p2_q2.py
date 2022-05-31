# Practical 2
# Q2

# Calculates the average of the numbers
def calculateAverage(no1, no2, no3, no4, no5):
    return (no1 + no2 + no3 + no4 + no5) / 5

# Asks for five numbers
no1 = float(input("Insert number 1: "))
no2 = float(input("Insert number 2: "))
no3 = float(input("Insert number 3: "))
no4 = float(input("Insert number 4: "))
no5 = float(input("Insert number 5: "))

# Prints the average
print("Average = %.2f" % calculateAverage(no1, no2, no3, no4, no5))
