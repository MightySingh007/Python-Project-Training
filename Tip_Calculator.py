bill = float(input("Bill amount: ₹"))
tip_pct = float(input("Tip percentage: "))
people = int(input("Number of people to split the bill: "))

tip = bill * (tip_pct / 100)
total = bill + tip
split_amount = total / people

print(f"Tip: ₹{tip:.2f}")
print(f"Total bill: ₹{total:.2f}")
print(f"Each person should pay: ₹{split_amount:.2f}")
