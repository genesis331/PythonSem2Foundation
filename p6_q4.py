# Practical 6
# Q4

# Asks for a number
num = int(input("Enter number: "))
# Loops till the input number
for i in range(2, num + 1):
    isPrime = True
    for j in range(2, i):
        # Checks if the number is a prime number
        if i % j == 0:
            isPrime = False
    if isPrime:
        # Prints the number if it is a prime number
        print(i)
