height = float(input("Enter your height in cm: "))



if height>=150:
    age = int(input("enter your age: "))
    if age > 18:
        print("You can ride the roller coaster and need to pay $12")
    elif age >= 12 and age <= 18 :
        print("You can ride the roller coaster and you will have to pay $7")
    else:
        print("You can ride the rollar coaster and you will have to pay $5")
else:
    print("You cannot ride the rollar coaster, sorry!")