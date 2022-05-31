# Practical 4
# Q3

# Asks for the hazard index
index = float(input("Hazard index: "))
# Prints the condition based on the hazard index
if 100 < index <= 200:
    print("Unhealthful")
elif 200 < index <= 275:
    print("First-stage haze alert")
elif index > 275:
    print("Second-stage haze alert")
else:
    print("Healthful")
