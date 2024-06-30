import csv
import random


def save_results(secret, attempts, success):
    headers = ["game number", "secret word", "attempts", "success"]
    with open("results.csv", "a+") as file:
        writer = csv.writer(file)
        reader = csv.reader(file)

        all_lines = len(list(reader))
        if all_lines == 0:
            writer.writerow(headers)

        writer.writerow([all_lines, secret, attempts, success])


MAX_ATTEMPTS = 6
WORDS = ["apple", "rapid", "panda", "hello", "world", "grape", "melon"]
secret_word = random.choice(WORDS)

print("Secret word: ", secret_word)

attempt = 0
while attempt < MAX_ATTEMPTS:
    attempt += 1
    guess = input(f"Enter your guess ({attempt}💔\\{MAX_ATTEMPTS}): ")
    while not (len(guess) == 5 and guess in WORDS):
        print("Invalid guess word. Try again.")
        guess = input("Enter your guess: ")

    if guess == secret_word:
        print("You guessed correctly!👏")
        save_results(secret_word, attempt, True)
        break

    zipped_words = zip(guess, secret_word)
    for g, h in zipped_words:
        if g == h:
            print(str(g).upper(), end="")
        elif g in secret_word:
            print(g, end="")
        else:
            print("*", end="")
    print()
else:
    print("You lost!😔")
    save_results(secret_word, attempt, False)
