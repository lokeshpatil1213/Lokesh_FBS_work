total_amount = 0

ticket_price = float(input("Enter ticket price per person: "))


for i in range(1, 6):
    age = int(input(f"Enter age of person {i}: "))

    if age < 12:
        amount = ticket_price * 0.70   
    elif age > 59:
        amount = ticket_price * 0.50   
    else:
        amount = ticket_price          

    total_amount += amount

print(f"Total ticket amount for 5 people = Rs. {total_amount}")
