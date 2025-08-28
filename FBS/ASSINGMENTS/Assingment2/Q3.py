feet = float(input("Enter distance in feet: "))
inches = float(input("Enter distance in inches: "))

total_inches = (feet * 12) + inches
cm = total_inches * 2.54
meters = cm / 100

print(f"Distance: {meters:.2f} meters or {cm:.2f} cm")
