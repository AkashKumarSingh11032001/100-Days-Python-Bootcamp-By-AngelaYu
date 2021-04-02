print("Welcom to the tip calculator.")

bill = eval(input("What was the total bill? (in Rupes) : "))

perTip = eval(input("What percentage tip would you like to give? 10, 12, or 15? "))
bill += perTip/100

split = eval(input("How many people to split the bill? "))
each_bill = round(bill/split,2)
print(f"Each have to pay: {each_bill} Rupes")