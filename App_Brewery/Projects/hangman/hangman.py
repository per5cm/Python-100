import random
from word_list import hangman_list, alphabet

print("Welcome to Hangman!\n")

# TODO 1 Randomly choose a word from the world_list and assign it to a variable called chosen_word. Then print it.


chosen_word = random.choice(hangman_list)
word_length = len(chosen_word)
print(f"Your chosen word is: {chosen_word} it has {word_length} letters in it.\n")

placeholder = ['_'] * word_length # pythonic way: placeholder = ["_" for _ in range word_length]
print(" ".join(placeholder))

# TODO 2 Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
# TODO 2.1 Create a "placeholder" with the same number of blanks as chosen_word.

while True:
    guess = input("\nGuess a letter in a word: ").lower()
    if guess not in alphabet:
        print("enter a letter...")
        continue

# TODO 3 Check if the letter the user guessed (guess) is one of the letters in the chosen_word. Print "Right" if it is "Wrong if its not."
# TODO 3.1 Create a "display" that puts the guess letter in the right placeholder.

    # option 1
    # for letter in chosen_word:
    #     if letter == guess:
    #         print("correct")
    #     else:
    #         print("wrong!")

    # option 2
    for index in range(word_length):
        letter = chosen_word[index]
        if letter == guess:
            placeholder[index] = guess
    print(" ".join(placeholder))

