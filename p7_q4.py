# Practical 7
# Q4

import random

list_of_numbers = []

# Generates a list of random numbers
for i in range(1000):
    list_of_numbers.append(random.randint(0,9))

counts = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

# Counts the number of times each number appears in the list
for i in range(len(list_of_numbers)):
    counts[list_of_numbers[i]] += 1

# Prints the number of times each number appears in the list
print("\nNumber\tFrequency")
print("-------\t-------")
for i in range(len(counts)):
    print("%d\t%d" % (i, counts[i]))
