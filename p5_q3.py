# Practical 5
# Q3

limit = 10000.00
# Asks for the amount of deposit
deposit = float(input("Deposit: "))
output = deposit
print("")
interestRate = 0.02
yearsSpent = 0
# Checks if the amount of deposit is greater than the limit
while output < limit:
    # Calculates the interest
    output += output * interestRate
    yearsSpent += 1
    # Prints the current amount
    print(f"Year {yearsSpent} --> RM{output:.2f}\n")
# Prints a summary
print(f"You'll need {yearsSpent} years to get at least RM{limit:.2f}")

# A wild duck appears!
#    __
#  <(o )___
#   ( ._> /
#    `---'   