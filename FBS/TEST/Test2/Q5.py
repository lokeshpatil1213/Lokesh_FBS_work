prices = []
for i in range(5):
    price = float(input(f"Enter price of product {i+1}: "))
    prices.append(price)

total = sum(prices)
gst = total * 0.18
total_bill = total + gst

print(f"Total bill including 18% GST = {total_bill}")
