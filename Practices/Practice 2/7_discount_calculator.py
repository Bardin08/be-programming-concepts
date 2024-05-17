THRESHOLD = 1000

price = float(input("Enter the price of the item: "))
quantity = int(input("Enter the quantity of the item: "))
discount = 0

if price * quantity > THRESHOLD:
    discount = 10
else:
    discount = 5

print(f"Discount: {discount}%. Price with discount: "
      f"${price * quantity * (1 - discount / 100):.2f}")
