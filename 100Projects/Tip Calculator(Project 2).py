print("Welcome to my Tip Calculator\n")
amount = float(input("What is the total bill amount? "))
no_of_people = int(input("How many people are splitting the bill? "))
tip = int(input("Enter the percentage of tip you want to give? 10%, 12% or 15%? "))
tip = tip / 100
individual_pay = (amount / no_of_people) * (1 + tip)
print("Each person should pay: ", round(individual_pay, 2))
