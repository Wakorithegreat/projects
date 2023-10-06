#JOHN KIBET  SCT211-0455/2022
#LEAP YEAR
year = int(input("enter a year of your choice: "))
print(year)
if year%4 ==0:
    if year%100 ==0:
        if year%400 == 0:
         print(f"{year} is a leap year")
        else:
            print(f"{year} is not a leap year")
    else:
        print(f"{year} is a leap year")
else:
    print("not leap year")

