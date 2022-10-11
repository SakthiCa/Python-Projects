#If the bill was $150.00, split between 5 people, with 12% tip.
print("*** Welcome to Split Per Person ***\n\n\n")
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60
bill_amt = input("What is the total amount ?$")
tip=input("what what percentage tip would u like to give 10,12 and 15 ?")
tip_perc = int(tip)/100
tot_amt = float(bill_amt)*tip_perc
tott_amt = tot_amt+float(bill_amt)
split = input("How many person would like to Split The bill ?")
split_amt = tott_amt/int(split)
round_amt = tott_amt//int(split)

print(f"\n\n\n${split_amt} per person should have to pay:\n")
print("The rounded values is given below👇")
print(f"\n${round_amt} per person should have to pay:")
print("(\n\n\n\n*****Thanks For having the time with us*****)")
