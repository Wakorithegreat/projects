#JOHN KIBET  SCT211-0455/2022
#SIMPLE CALCULATOR
sign = input("choose either of the signs +,-,* or /: ")
num1 =int(input("enter the first number:"))
num2 =int(input("enter the second number: "))
#addition
if sign == '+':
    print("addition: ",num1 + num2)

#subtraction 
elif sign == '-':
    print("subtraction: ",num1 - num2)

#multiplication
elif sign == '*':
    print("multiplication: ",num1 * num2)

#division
elif sign == '/':
    print("division: ",num1 / num2)

else:
    print("invalid operator")



