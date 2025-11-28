print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tipPercent = float(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))

# If the bill was $150.00, split between 5 people, with 12% tip.
# Each person should pay:
# (150.00 / 5) * 1.12 = 33.6

tip_as_percent = tipPercent / 100
total_tip_amount = bill * tip_as_percent
tota_bill = bill + total_tip_amount
bill_per_person = tota_bill / people
final_amount = round(bill_per_person, 2)

print(f"Each person should pay {final_amount}")