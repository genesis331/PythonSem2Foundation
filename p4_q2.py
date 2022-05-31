# Practical 4
# Q2

# Asks for ACT score
actScore =  float(input("ACT Score: "))
# Asks if the student graduated in the top half of ACT
graduateInTopHalf = bool(True if input("Graduate in top half of ACT: ") == "Y" else False)
# Asks for the GPA score
gpa = float(input("GPA: "))

# Checks if at least two conditions are met
if (actScore >= 18, gpa >= 2.0, graduateInTopHalf == True) >= 2:
    print("You are eligible to play a sport.")
else:
    print("You are not eligible to play a sport.")
