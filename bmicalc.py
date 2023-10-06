#JOHN KIBET  SCT211-0455/2022
#BMI CALCULATOR
height = float(input("enter your height: "))
weight = int(input("enter your weight: "))
bmi = int(weight/height**2)
print("you're BMI is: ",bmi)
if bmi < 18.5:
    print("you are underweight!")
elif bmi >18.5 < 25:
    print("you have a normal weight!")
else:
    print("you are overweight!")
