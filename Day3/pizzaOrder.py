#Build Automatic pizza order program
'''
Based on user's order, work out their final bill
Small Pizza : $15
Medium Pizza : $20
Large Pizze : $25

Pepperoni for small pizza : +$2
Pepperoni for medium/large pizza : +$3
Extra cheese for any size pizza : +$1

Example Input:
size = "L"
add_pepperoni = "Y"
extra_cheese = "N"

Example Output:
Your final order bill is: $28.
'''


print("Welcome to Python Pizza Deliveries")
size = input("What size pizza do you want? S, M or L: ")
add_pepperoni = input("Do you want pepperoni? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")

'''
bill =0;

if size== 'L':
    bill += 25
    if add_pepperoni == 'Y':
        bill+= 3
        if extra_cheese == 'Y':
            bill += 1
            print(f"Your final order bill is ${bill}.")
        else:
            print(f"Your final order bill is ${bill}.")
    else:
        print(f"Your final order bill is ${bill}.")
elif size == 'M':
    bill += 20
    if add_pepperoni == 'Y':
        bill+= 3
        if extra_cheese == 'Y':
            bill += 1
            print(f"Your final order bill is ${bill}.")
        else:
            print(f"Your final order bill is ${bill}.")
    else:
        print(f"Your final order bill is ${bill}.")
elif size == 'S':
    bill += 15
    if add_pepperoni == 'Y':
        bill+= 2
        if extra_cheese == 'Y':
            bill += 1
            print(f"Your final order bill is ${bill}.")
        else:
            print(f"Your final order bill is ${bill}.")
    else:
        print(f"Your final order bill is ${bill}.")
'''

bill = 0
if size == 'S':
    bill += 15
elif size == 'M':
    bill += 20
elif size == 'L':
    bill += 25

if add_pepperoni =="Y":
    if size == 'S':
        bill += 2
    else:
        bill += 3


if extra_cheese == 'Y':
    bill += 1

print(f"Your final order bill is ${bill}.")
