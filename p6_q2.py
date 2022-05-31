# Practical 6
# Q2

# Asks for starting and ending number
startNum = int(input("START: "))
endNum = int(input("END: "))
# Loops through the numbers
for i in range(startNum, endNum + 1):
    print("")
    for j in range(1, 13):
        # Calculates the product
        print("%d x %d = %d" % (i, j, i * j))
