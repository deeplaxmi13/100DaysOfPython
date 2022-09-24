print("Welcome to the TREASURE ISLAND. Your mission is to find the treasure")


print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/______/_
*******************************************************************************
''')

leftOrRight = input('You\'re at a cross road, where do you wanna go to? Type "left" or "right"?: ').lower()
if leftOrRight == 'left' :
    swimOrWait = input("You\'ve come to a lake. There is an island in the middle of the lake. Do you wanna swim or wait for the boat? Type 'wait' to wait and 'swim' to swim across: ").lower()
    if swimOrWait == 'wait':
        whichDoor = input("You\'ve come to a lake. There is a house with three doors. Which door you wanna enter? Red, Yellow or Blue: ").lower()
        if whichDoor == "yellow":
            print("You have found the treasure. You win!")
        elif whichDoor == "blue":
            print("Your have chosed a room of beast. Game Over!")
        elif whichDoor == "red":
            print("You have chosed a room full of fir. Game Over!")
        else:
            print("You chose a door that doesn't exist. Game Over!")
    else:
        print("You got attacked by an angry trout. Game Over!")
else:
    print("You fell into a hole. Game Over !!!")