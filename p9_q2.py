# Practical 9
# Q2

# Opens order.txt and allows read-only access
with open("order.txt", "r") as f:
    splitOrderData = []
    totalPayment = 0
    # Reads the file, splits every record by newline then stores it in a variable
    order = f.read().split()
    for i in range(len(order)):
        # Splits the record by delimiter '|'
        splitOrderData.append(order[i].split("|"))
    for i in range(len(splitOrderData)):
        # Calculates the total payment
        totalPayment += int(splitOrderData[i][1]) * float(splitOrderData[i][2])
    # Prints the total payment
    print('Total Order: RM%.2f' % totalPayment)
