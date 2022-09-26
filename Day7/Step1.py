#Step1

import random


word_list = ["ardvark","baboon","camel"]

'''
TODO 1: Randomly choose a word from the word_list and assign it to a variable called choosen_word

TODO 2: Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.

TODO 3: Check if the letter the user guessed is one of the letters in the choosen word.
'''

choosen_word = random.choice(word_list)

guess = input("Guess a letter: ").lower()

for letter in choosen_word:
    if guess == letter:
        print("True")
    else:
        print("False")



