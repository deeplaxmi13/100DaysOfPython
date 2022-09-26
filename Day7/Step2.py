import random

word_list = ["ardvark","baboon","camel"]

choosen_word = random.choice(word_list)

guess = input("Guess a letter: ").lower()



#Step2

'''
TODO 1: Create an empty list called display.
        For each letter in the chosen_word, add a "_" to 'display.
        So if the chosen word was "apple", display should be ["_","_","_","_","_"] with 5 "_" representing each letter to guess.


TODO 2: Loop through each position in the chosen_word;
        If the letter at that position matches 'guess' then reveal that letter in the display at that position 
        eg: If user guessed 'p' and the chosen word was 'apple' then display should be ["_","p","p","_","_"].


TODO 3: Print 'display' and you should see the guess letter in the correct position and every other letter replace 
        with "_".

'''

display = []

word_length = len(choosen_word)
for i in range(word_length):
    display += "_"

for i in range(word_length):
    if guess == choosen_word[i]:
        display[i] = guess

print(display)








