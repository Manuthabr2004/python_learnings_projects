#cover f-string,Type-casting,mathematical-Calculations
print("Welcome To Bill Calculator!.")
bill = int(input("Enter the amount to pay $"))
tip = int(input("How much tip would you like to give? 10 , 11 , 12- "))
bill_with_tip = bill + tip / 100
people = int(input("Enter how many number of people to share bill:"))
total_bill = bill_with_tip / people
final_bill = round(total_bill , 2)
print(f" Your total bill is = ${final_bill}")