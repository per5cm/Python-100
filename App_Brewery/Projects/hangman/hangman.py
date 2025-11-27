import random
from word_list import hangman_list

print("Welcome to Hangman!\n")

# TODO 1 Randomly choose a word from the world_list and assign it to a variable called chosen_word. Then print it.

chosen_word = random.choice(hangman_list)
word_length = len(chosen_word)
print(f"Your chosen word is: {chosen_word} it has {word_length} letters in it.\n")

# TODO 2 Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.

while True:
    guess = input("Guess a letter in a word: ").lower()

# TODO 3 Check if the letter the user guessed (guess) is one of the letters in the chosen_word. Print "Right" if it is "Wrong if its not."

    guess_list = []

    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            print("correct")
        elif letter != guess:
            print("wrong!")

    # option 2
    # for letter in chosen_word:
    #     if letter == guess:
    #         print("right")
    #     else:
    #         print("Wrong")