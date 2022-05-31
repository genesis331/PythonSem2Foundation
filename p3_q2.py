# Practical 3
# Q2

# Asks for employee number, hours worked and hourly rate
employee_number = str(input("Enter employee's number: "))
hours_worked = float(input("Enter hours worked: "))
pay_rate = float(input("Enter hourly pay rate: "))
total_pay = 0

# Checks if hours worked is greater than 40
if hours_worked > 40:
    # Calculates the overtime hours
    overtime_hours = hours_worked - 40
    # Calculates the overtime pay
    overtime_pay = overtime_hours * pay_rate * 1.5
    # Checks if hours worked is greater than 100
    if hours_worked > 100:
        # Calculates the total pay with an extra 200 bonus
        total_pay = overtime_pay + (40 * pay_rate) + 200
    else:
        # Calculates the total pay
        total_pay = overtime_pay + (40 * pay_rate)
else:
    # Calculates the total pay
    total_pay = hours_worked * pay_rate

# Prints the total pay
print("Total Pay: %.2f" % total_pay)
