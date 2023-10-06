#JOHN KIBET  SCT211-0455/2022
#TIP CALCULATOR
bill = float(input("Enter the total bill: "))
tips = float(input("do you choose 10,12,15: "))
no_people = int(input("number of people splitting the bill? "))

total_tip = round(((tips/100)*bill)/no_people ,2) 

print("Each persons tip is: ",total_tip)