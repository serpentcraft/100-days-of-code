# Day 2 - Tip Calculator

print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? "))
tip = int(input("How much tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill? "))

each_bill = bill / people
total = each_bill * (1 + tip / 100)
total_bill = round(total, 2)

print(f"Each person should pay: ${total_bill}")
