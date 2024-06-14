"""
Creates the result_list difference between two lists
"""
import random

sequence = range(1, 101)
list_1 = random.choices(sequence, k=25)
list_2 = random.choices(sequence, k=25)

result_list = [n for n in list_1 if n not in list_2]

print(result_list)

K = 3
N = 5

[print(n) for n in result_list if n % K == 0 and n % N == 0]

""" 
# Game Mechanics:
#   The program selects a random word from a predefined list;                          ✅
#   The word is displayed as a series of underscores, representing each letter;        ✅
#   Players guess one letter at a time;                                                ✅
#   If the guessed letter is in the word, reveal its position(s);                      ✅
#   If the guess is incorrect, add a part to the hangman drawing;                      ✅
#   Players continue until they guess the word or the hangman drawing is complete.     ✅
"""

MAX_ATTEMPTS = 8
WORDS = ["apple", "rapid", "panda", "hello", "world", "grape",
         "melon", "python", "java", "swift", "csharp", "javascript"]
secret_word = random.choice(WORDS)
print("Secret word: ", secret_word)

user_word = list("_" * len(secret_word))
print(" ".join(user_word))

lives = MAX_ATTEMPTS
while lives > 0 and "_" in user_word:
    user_letter = input(f"Enter your guess ({lives}❤️): ")
    while not user_letter.isalpha() or len(user_letter) != 1:
        print("Invalid guess. Try again.")
        user_letter = input("Enter your guess: ")

    if user_letter in secret_word:
        for index, letter in enumerate(secret_word):
            if user_letter == letter:
                user_word[index] = user_letter
    else:
        lives -= 1
        print("You lost a life💔")

    print(" ".join(user_word))

if "_" not in user_word:
    print("You won!")
else:
    print("You lost")

# -- zip --

l1 = [1, 2, 3, 4, 5]
l2 = ["1", "2", "3", "4"]

print(list(zip(l1, l2, l1, l2)))
