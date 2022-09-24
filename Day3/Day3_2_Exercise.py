#write a program that works out whether if a given year is a leap year. A normal year has 365 days, leap year has 366 days, with an extra day in Februaray. 


print("Welcome to Leap Year Checker")

year = int(input("Enter the year you want to check: "))

if year%4 == 0:
    if year % 100 ==0:
        if year % 400 ==0 :
            print(" leap year")
        else:
            print("Not a leap year")
    else:
        print("Leap year")
else:
    print("Not a leap year")

