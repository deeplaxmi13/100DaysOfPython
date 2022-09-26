import random
word_list = ["ardvark","baboon","camel"]
choosen_word = random.choice(word_list)
word_length = len(choosen_word)

display = []
for i in range(word_length):
    display += "_"

#Step 3

'''
TODO 1: Use a while loop to let the user guess again. The loop should only stop once the user has guessed all the letters in the chosen_word and 'display' has no more blanks("_"). Once all the balnks are filled you can tell the user, they have won.

'''



end_of_game = False

while not end_of_game:
    guess = input("Guess a letter: ").lower()
    for i in range(word_length):
        if guess == choosen_word[i]:
            display[i] = guess
    print(display)
    if "_" not in display:
        end_of_game = True
        print("You win!")

print(display)