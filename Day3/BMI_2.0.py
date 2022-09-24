print("Welcome to BMI Calculator Version 2")

weight = float(input("Enter your weight in kg: "))

height = float(input("Enter your height in cm: "))

BMIIndex = round(weight/(height ** 2))

if BMIIndex < 18.5:
    print(f"Your BMI value is {BMIIndex} and indicates that you are underweight")
elif BMIIndex < 25:
    print(f"Your BMI value is {BMIIndex} and indicates that you have a normal weight")
elif BMIIndex < 30:
    print(f"Your BMI value is {BMIIndex} and indicates that you are overweight")
elif BMIIndex < 35:
    print(f"Your BMI value is {BMIIndex} and indicates that you are obese")
else:
    print(f"Your BMI value is {BMIIndex} and you are clinically obese")