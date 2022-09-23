print("Welcome to the Tip Calculator")

totalBill = float(input("what was your total bill : $ "))

tipPercentage = int(input("what percentage tip would you like to give ? 10, 12 or 15 ? : "))

spiltBill = int(input("How many people to split the bill : "))



totalBillEachPerson = round((totalBill + ((tipPercentage/100)* totalBill))/spiltBill, 2)

print(f"Each person have to pay {totalBillEachPerson} ")