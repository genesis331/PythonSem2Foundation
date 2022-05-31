# Practical 2
# Q1

# Converts the input from foot to meter
def footToMeter(foot):
    return foot / 3.2808

# Converts the input from meter to foot
def meterToFoot(meter):
    return meter * 3.2808

# Asks for foot and meter
inputFoot = float(input("Insert foot: "))
inputMeter = float(input("Insert meter: "))

# Prints the result after converting
print("%.2f foot = %.2f meter" % (inputFoot, footToMeter(inputFoot)))
print("%.2f meter = %.2f foot" % (inputMeter, meterToFoot(inputMeter)))
