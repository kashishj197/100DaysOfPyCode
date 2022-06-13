# # Tip calculator # #

total_amt = float(input("What was the total bill? $"))
percentage_amt = int(input("What percentage of tip you want to give 10, 12 or 15? "))
num_of_people = int(input("What was the number of people in the party? "))
tip_amt = (total_amt // num_of_people) * (percentage_amt / 100)

print(f"The tip per person will be of {round(tip_amt, 2)}")
