import random
from word_list import hangman_list

print("Welcome to Hangman!\n")

# TODO 1 Randomly choose a word from the world_list and assign it to a variable called chosen_word. Then print it.

chosen_word = random.choice(hangman_list)
print(f"Your chosen word is: {chosen_word}")

# TODO 2 Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.

guess = input("Guess a letter in a word: ").lower()

# TODO 3 Check if the letter the user guessed (guess) is one of the letters in the chosen_word. Print "Right" if it is "Wrong if its not."


for letter in chosen_word:
    if guess == chosen_word:
        print("correct")