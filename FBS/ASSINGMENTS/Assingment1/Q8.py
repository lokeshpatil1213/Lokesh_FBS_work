days = int(input("Enter number of days: "))
years = days // 365
weeks = days % 365 // 7
days_left = (days % 365) % 7
print(f"{years}years, {weeks} weeks, {days_left} days")