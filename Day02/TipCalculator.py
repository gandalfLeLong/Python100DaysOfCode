#Small program calculating how to split the bill using the total, the tip pourcentage and the number of payers

#gathering inputs
print("Welcome to the tip calculator")
total = input("What was the total bill : $")
tip = input("How much tip would you like to give ? 10, 12 or 15 ? ")
numberOfPeople = input("How many people to split the bill ? ")

#convertion type
total = float(total)
tip = "1." + tip
tip = float(tip)
numberOfPeople = float(numberOfPeople)

#calculate and printing the result
res = ((total * tip) / numberOfPeople)
res = round(res, 2)
print(f"Each person should pay : ${res}")
