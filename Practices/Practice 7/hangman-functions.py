import random

""" 
# Game Mechanics:
#   The program selects a random word from a predefined list;                          ✅
#   The word is displayed as a series of underscores, representing each letter;        ✅
#   Players guess one letter at a time;                                                ✅
#   If the guessed letter is in the word, reveal its position(s);                      ✅
#   If the guess is incorrect, add a part to the hangman drawing;                      ✅
#   Players continue until they guess the word or the hangman drawing is complete.     ✅
"""


def get_secret_word():
    words = ["apple", "rapid", "panda", "hello", "world", "grape",
             "melon", "python", "java", "swift", "csharp", "javascript"]
    word = random.choice(words)
    return word


def get_user_input():
    guess = input(f"Enter your guess ({lives}❤️): ")
    while not guess.isalpha() or len(guess) != 1:
        print("Invalid guess. Try again.")
        guess = input(f"Enter your guess ({lives}❤️): ")

    return guess


def replace_guessed_letters(secret, letter, word):
    for index, l in enumerate(secret):
        if letter == l:
            word[index] = letter


MAX_ATTEMPTS = 8
secret_word = get_secret_word()
print("Secret word: ", secret_word)

user_word = list("_" * len(secret_word))
print(" ".join(user_word))

lives = MAX_ATTEMPTS
while lives > 0 and "_" in user_word:
    user_letter = get_user_input()

    if user_letter in secret_word:
        replace_guessed_letters(secret_word, user_letter, user_word)
    else:
        lives -= 1
        print("You lost a life💔")

    print(" ".join(user_word))

if "_" not in user_word:
    print("You won!")
else:
    print("You lost")

