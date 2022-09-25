'''
you are going to write a program that calculates the sum of all the even numbers from 1 to 100.
'''

total =0

for number in range(2,101,2):
    total+= number
print(f"Sum of all even numbers is {total}")

total1 =0
for number in range(1,101):
    if number % 2 == 0:
        total1 += number
print(f"Sum of all even numbers is {total1}")
