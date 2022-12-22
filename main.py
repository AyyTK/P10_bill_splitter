# If the bill was $150.00, split between 5 people, with 12% tip.
# Each person should pay (150.00 / 5) * 1.12 = 33.6
# Format the result to 2 decimal places = 33.60
# Thus everyone's share of the total bill is $30.00 plus a $3.60 tip.
# Tip: There are 2 ways to round a number. You might have to do some Googling to solve this

bill = int(input("Type your total here:  "))  # (text output is extra for assignment)
# tip = 0.2 (original)
tip = int(input("Type the percentage you would like to tip here  "))  # (extra)
# total = bill * tip (original)
tip2 = bill * tip / 100  # (extra credit)
total = bill + tip2  # (extra credit)
print(float(total))