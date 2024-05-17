import random

number = random.randint(1, 100)

guess = int(input("Guess the number (1-100): "))

if guess == number:
    print("Congratulations! You guessed the number.")
elif guess < number:
    print("The number is higher.")
else:
    print("The number is lower.")

"""
Add a loop to allow the user 
to guess multiple times until they guess the number.
"""
