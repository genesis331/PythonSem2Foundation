# Practical 7
# Q3

nums = []
squaredNums = []

# Asks for an integer and appends it to the list
nums.append(int(input("Integer: ")))
while True:
    # Checks if the last number is 0
    if (nums[len(nums) - 1] == 0):
        # Removes the last number from the list
        nums.pop()
        # Breaks the loop
        break
    else:
        nums.append(int(input("Integer: ")))

# Squares each number in the list and appends it to the list
for i in range(len(nums)):
    squaredNums.append(nums[i] ** 2)

# Prints the list of numbers and the list of squared numbers
print("\nInteger\tSquared")
print("-------\t-------")
for i in range(len(nums)):
    print("%d\t%d" % (nums[i], squaredNums[i]))
