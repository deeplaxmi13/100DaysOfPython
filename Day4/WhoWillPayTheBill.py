'''
You are going to write a program which will select a random name from a list of names. The person selected will have to pay  for everybody's food bill.

Important: You are not allowed to use choice() function

Example Input:
Angela, Ben, Jenny, Michael, Chloe


Example Output:
Michael is going to pay the bill

'''
import random
namesString = input("Give me everbody's name, seperate by a comma: ")
names = namesString.split(", ")
print(names)
# print(len(names))

pickedName = random.randint(0,len(names)-1)
print(f"{names[pickedName]} will have to pay the bill. ")



NamesPay= random.choice(names)
print(f"{NamesPay} will have to pay the bill. ")