print("welcom to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("How much tip would you like to pay? 10, 12 or 15? "))
people = int(input("how many people to split the bill?"))
tip_as_percent = tip / 100
total_tip_amount = bill * tip_as_percent
total_bill = bill + total_tip_amount
bill_per_person = total_bill / people
final_amount = "{:.2f}".format(bill_per_person)
print(f"Each person should pay {final_amount}")