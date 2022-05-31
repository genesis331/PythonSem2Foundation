# Practical 3
# Q1

# Asks for two numbers
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
# Calculates the sum
sum = num1 + num2
# Calculates the difference
diff = num1 - num2
# Calculates the product
prod = num1 * num2
# Prints the results
print("Sum: %d" % sum)
print("Difference: %d" % diff)
print("Product: %d" % prod)
# Checks if num2 is a zero
if num2 != 0:
    # Calculates and prints the quotient
    quot = num1 // num2
    print("Quotient: %d" % quot)
else:
    # Prints warning message
    print("Quotient: Division by zero is not possible")
