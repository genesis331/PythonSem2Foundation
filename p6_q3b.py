# Practical 6
# Q3 (alternative)

# Asks for number of lines
lineNum = int(input("Lines: "))
print("")
# Prints the lines using loops
for i in range(lineNum):
    for j in range(lineNum - i - 1):
        print(" ", end="")
    for k in range(i * 2 + 1):
        print("*", end="")
    print("")
