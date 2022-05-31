# Practical 6
# Q1

total = 0
# Loops five times
for i in range(5):
    # Asks for a number
    num = int(input("Enter number %d: " % (i + 1)))
    # Adds the number to the total
    total += num
# Calculates the average
avg = total / 5
# Prints the average
print("Average: %.2f" % avg)
