# Test 2
# Q2

itemList = [
    ["Christmas Tree", 60.00, 10],
    ["Bell", 30.00, 100],
    ["Candles Pack", 12.00, 250],
    ["Garland", 26.00, 50],
]

# Loops and prints the item list
print("Item List:")
for i in range(len(itemList)):
    print("%d." % (i + 1),itemList[i][0])

# Asks the user to select an item
itemOption = int(input("\nEnter item option: "))

while itemOption != 9999:
    # Asks the user to enter the quantity
    numOfUnits = int(input("Enter the number of unit(s): "))
    # Checks if the item stock is enough
    if itemList[itemOption - 1][2] < numOfUnits:
        print("Error: There's not enough item.\nYou can only purchase up to a maximum of %d unit(s)." % itemList[itemOption - 1][2])
    else:
        # Subtracts the number of units from the item stock
        itemList[itemOption - 1][2] -= numOfUnits
        print("Total price: RM%.2f" % (itemList[itemOption - 1][1] * numOfUnits))
    
    itemOption = int(input("\nEnter item option: "))

# Asks the user if they want to see the summary of the item list
toCheckInv = input("Do you want to check the inventory? (yes/no): ")
if toCheckInv == "yes":
    # Prints the item list summary
    print("-" * 40)
    print("Item" + " " * 26 + "Unit")
    print("-" * 40)
    for i in range(len(itemList)):
        print("%s" % itemList[i][0] + " " * (30 - len(itemList[i][0])) + "%d" % itemList[i][2])
