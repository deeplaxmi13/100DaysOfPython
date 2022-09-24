'''
Write a program that testes the compatibility between two people. 

Take both people's names and check for the number of times the latters in the word TRUE occurs. Then check for the number of times the letters in the world LOVE occurs. The combine thee numbers to make a two digit number

'''

print("Welcome to the love calculator!")

yourName = input("Enter your name: ").lower()
theirName = input("Enter their name: ").lower()
combinedName = yourName+theirName
score = 0

countTrue = 0
countLove = 0

# countLove += combinedName.count("l")
# countLove += combinedName.count("o")
# countLove += combinedName.count("v")
# countLove += combinedName.count("e")

# countTrue += combinedName.count("t")
# countTrue += combinedName.count("r")
# countTrue += combinedName.count("u")
# countTrue += combinedName.count("e")

for i in range(len(combinedName)):
    if  combinedName[i] == 'l' or combinedName[i] == 'o' or combinedName[i] == 'v' or combinedName[i] == 'e':
        countLove += 1
    if combinedName[i] == 't' or combinedName[i] == 'r' or combinedName[i] == 'u' or combinedName[i] == 'e':
        countTrue += 1




score = int(str(countTrue) + str(countLove))

if score < 10 or  score > 90:
    print(f"Your score is {score}, you go together like coke and mentos.")
elif score > 40 and score < 50 :
    print(f"Your score is {score} and you are alright together")
else:
    print(f"Your score is {score}")
