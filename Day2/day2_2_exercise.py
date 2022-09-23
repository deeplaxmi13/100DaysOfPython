#create a program using maths and f-strings that tells us how many days, weeks and months we have if we live until 90 years old.

age = int(input("Enter your current age: "))

years_remaining = 90 - age

days = years_remaining * 365

weeks = years_remaining * 52

months = years_remaining * 12

print(f"You have {days} days, {weeks} weeks, {months} months left")