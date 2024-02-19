DISCOUNT = 0.1
total_price = 0
number = int(input("Number of items: "))
while number < 0:
      print("Invalid number of items!")
      number = int(input("Number of items: "))
for i in range(0, number):
    price = float(input("Price of item:"))
    total_price += price
if total_price > 100:
    total_price = total_price * (1 - DISCOUNT)

print(f"Total price for {number} items is ${total_price:.2f}")



