#PEMDAS
#Parenthesis ()
#Exponents **
#Multiplication *
#Division /
#Addition +
#Subraction -
#// floor for rounding down


print("Welcome to the tip calculator.")
bill_amount = float(input("What was the total bill?"))
percent_tip = int(input("What percentage tip would you like to give? 10, 12, or 15"))
people_split = int(input("How many people to split the bill?"))

calculate_bill_amount = (bill_amount + bill_amount * (percent_tip * .01)) / people_split
calculate_bill_amount = round(calculate_bill_amount,2)
print(f"Each person should pay: ${calculate_bill_amount}")
