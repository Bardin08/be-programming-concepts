import random

words = ["apple", "rapid", "panda", "hello", "world", "grape", "melon"]
secret_word = random.choice(words)

print("Secret word: ", secret_word)

attempts = 0
while attempts < 5:
    attempts += 1
    guess = input("Enter your guess: ")
    while not (len(guess) == 5 and guess in words):
        print("Invalid guess word. Try again.")
        guess = input("Enter your guess: ")

    if guess == secret_word:
        print("You guessed correctly!")
        break

    zipped_words = zip(guess, secret_word)
    for g, h in zipped_words:
        if g == h:
            print("Letter matched: ", g)
        elif g in secret_word:
            print("Letter not matched(position): ", g)
        else:
            print("Letter not matched: ", g)
else:
    print("You have used all your attempts. The secret word was.")
