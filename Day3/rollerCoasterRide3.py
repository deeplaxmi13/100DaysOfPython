height = float(input("Enter your height in cm: "))

bill = 0


if height>=150:
    age = int(input("enter your age: "))
    if age > 18:
        print("Adult tickets are $12")
        bill = 12
    elif age >= 12 and age <= 18 :
        print("Youth tickets are $7")
        bill = 7
    else:
        print("Child tickets are $5")
        bill = 5
    
    wantsPhoto = input("Do you want your photos to be taken? ")
    if wantsPhoto == "Y":
        bill += 3
        print(f"Your total bill is {bill}")
    else:
        print(f"Your bill is {bill}")
else:
    print("You cannot ride the rollar coaster, sorry!")