import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
'''


scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

lists = [rock, paper, scissors]
print(f"{rock}\n{scissors}\n{paper}")

userInput = input("Choose rock, paper or scissors: ").lower()
if userInput == "rock":
    userInput = rock
elif userInput == "paper":
    userInput = paper
elif userInput == "scissors":
    userInput = scissors
else:
    print("You entered a wrong choice")


computerChoice = random.choice(lists)



# Rock wins against scissors
# Paper wins agants rock
# Scissors wins against paper

print("Your choice: ")
print(userInput)
print("computerChoice:")
print(computerChoice)

if userInput == rock and computerChoice == scissors:
    print("You win!")
elif userInput == rock and computerChoice == paper:
    print("You Lose")
elif userInput == paper and computerChoice ==  rock:
    print("You win!")
elif userInput == paper and computerChoice ==  scissors:
    print("You Lose")  
elif userInput == scissors and computerChoice ==  paper:
    print("You win!")
elif userInput == scissors and computerChoice ==  rock:
    print("You Lose")  
elif userInput == computerChoice:
    print("Match Drawn!") 


#Another easy way of doing

# userInput = int(input("What do you choose?  Type 0 for Rock, Type 1 for Paper and Type 2 for Scissors:   "))

# computerChoice = random.randint(0,2)

# print(f"User Choice : {userInput}\nComputer Choice : {computerChoice}")

#this logic uses numbers instead of images/Ascii art



