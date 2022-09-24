print("Welcome to Roller Coaster Ride")


height = float(input("Enter your height: "))
bill = 0

if height > 120 :
    age = int(input("Enter your age: "))
    if age < 12:
        bill += 5
    elif age <= 18:
        bill += 7
    elif age >= 45 and age <= 55:
        bill += 0
    else:
        bill += 12

    want_photos = input("Do you want photos ? Y or N: ")
    if want_photos == 'Y':
        bill += 3
        print(f"Your total bill is ${bill}")
    else:
        print(f"Your total bill is ${bill}")
else:
    print("Sorry you cannot ride the roller coaster")
