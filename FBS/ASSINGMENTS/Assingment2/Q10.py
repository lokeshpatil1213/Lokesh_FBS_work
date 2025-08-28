num = int(input("Enter a three-digit number: "))

d1 = num % 10
d2 = (num // 10) % 10
d3 = num // 100

reverse = (d1 * 100) + (d2 * 10) + d3
print("Reversed number:", reverse)
