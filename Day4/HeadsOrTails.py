'''
You are going to create a virtual coin toss program. It will randomly tell the user "Heads" or "Tails". 

Important note: The first letter should be capitalised and spelt exactly like in the example. eg Heads,not heads.

There sare many ways of doing this. But to practice what we learnt in the last lesson, you should generate a random number, either 0 or 1. Then use that number to print out Heads or Tails.

eg:
1 means Heads
0 means Tails


'''

import random as r

# randomNumber = r.randrange(0,2)
# if randomNumber == 1:
#     print("Heads")
# elif randomNumber == 0:
#     print("Tails")

randomInteger = r.randint(0,1)
if randomInteger == 1:
    print("Heads")
else :
    print("Tails")