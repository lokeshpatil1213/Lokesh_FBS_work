P = float(input("Enter a Principal:"))
T = float(input("Enter a Time:"))
R = float(input("Enter a Rate:"))

CI = P*((1+R/100)**T)-P
print("Compound Interest:",CI)