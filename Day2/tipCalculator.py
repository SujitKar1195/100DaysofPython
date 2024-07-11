print("Welcome to the Tip Calculator!")
total_bill = float(input("What was the total bill? $: "))
tip_percent = int(input("What percentage tip would you like to give? 10, 12, or 15? %: "))
people_to_split = int(input("How many people to split the bill? : "))
#logic
tip_amount = (total_bill * (tip_percent / 100))
amount_to_pay = (total_bill + tip_amount) / people_to_split
#answer
print("Each person should pay: ${amount}".format(amount=round(amount_to_pay, 2)))

