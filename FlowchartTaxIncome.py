#minutes into hours
minutes = 250

hours = minutes // 60
remaining_minutes = minutes % 60

print("Hours:", hours)
print("Minutes:", remaining_minutes)

#flowchart Program


income = float(input("Enter your taxable income: "))

if income <= 20000:
    tax = 0.02 * income
elif income <= 50000:
    tax = 400 + 0.025 * (income - 20000)
else:
    tax = 1150 + 0.035 * (income - 50000)

print("Tax:", tax)
