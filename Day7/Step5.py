#Step5

import random
from hangman_words import word_list
from hangman_art import logo, stages


'''
TODO 1: Update the word list to use the 'word_list' from hangman_words.py

TODO 2: Import the stages from hangman_art.py and make this error go away

TODO 3: Import the logo from hangman_art.py and print it at the start of the game

TODO 4: If the user has entered a letter they've already guessed, print the letter and let them know

'''

print(logo)

end_of_game = False
#word_list = hangman_words.word_list
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

display = []
for _ in range(word_length):
    display += "_"

lives = 6


while not end_of_game:
    guess = input("Guess a letter: ").lower()
    if guess in display:
        print(f"You have already guessed the letter  {guess}")
        
    for position in range(word_length):
        if chosen_word[position] == guess:
            display[position] = chosen_word[position]

    if guess not in chosen_word:
        print(f"You guessed {guess}, that is not present in the word. You lose a life")
        lives -= 1 
        if lives == 0:
            end_of_game = True
            print("You lose")

    print(f"{' '.join(display)}")    

    if "_" not in display:
        end_of_game = True
        print("You win.")
    

    print(stages[lives])