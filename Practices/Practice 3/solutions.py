# 1. Number Sequence:

# For loop (1 to 20)
for num in range(1, 21):
    print(num)

# While loop (20 to 1)
num = 20
while num >= 1:
    print(num)
    num -= 1

# 2. Sum of Numbers:
total = 0
number = int(input("Enter a number (0 to quit): "))

while number != 0:
    total += number
    number = int(input("Enter a number (0 to quit): "))

print("Sum of numbers:", total)

# 3. Multiplication Table (Input Validation):
while True:
    number = int(input("Enter a number between 1 and 12: "))
    if 1 <= number <= 12:
        break
    else:
        print("Invalid input. Please try again.")

print(f"Multiplication table for {number}:")
for i in range(1, 13):
    print(f"{number} x {i} = {number * i}")

# 4. Guess the Number (Enhanced):
import random

number = random.randint(1, 100)
guesses = 0
max_guesses = 5

while guesses < max_guesses:
    guess = int(input("Guess the number (1-100): "))
    guesses += 1

    if guess == number:
        print(f"Congratulations! You guessed it in {guesses} attempts.")
        break
    elif guess < number:
        print("Too low!")
    else:
        print("Too high!")

if guesses == max_guesses:
    print(f"Sorry, you ran out of guesses. The number was {number}.")

# 5. Factorial with Validation:
while True:
    number = int(input("Enter a non-negative integer: "))
    if number >= 0:
        break
    else:
        print("Invalid input. Please enter a non-negative integer.")

factorial = 1
for i in range(1, number + 1):
    factorial *= i

print(f"Factorial of {number} is {factorial}")

# 6. Fibonacci Sequence with Limit:
limit = int(input("Enter a limit for the Fibonacci sequence: "))
a, b = 0, 1

while a <= limit:
    print(a)
    a, b = b, a + b

# 7. Average Calculator (with Validation):
total = 0
count = 0

while True:
    number = float(input("Enter a number (negative to quit): "))
    if number < 0:
        break
    total += number
    count += 1

if count > 0:
    average = total / count
    print("Average:", average)
else:
    print("No positive numbers were entered.")

# 8. Prime Number Checker (Range):
start = int(input("Enter the starting number: "))
end = int(input("Enter the ending number: "))

print(f"Prime numbers between {start} and {end}:")
for num in range(start, end + 1):
    if num > 1:
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                break  # Not prime
        else:  # No divisors found, it's prime
            print(num)


# 9. Pattern Printing (Customizable):

char = input("Enter a character: ")
rows = int(input("Enter the number of rows: "))
pattern_type = input("Enter pattern type (triangle, rectangle, diamond): ")

for i in range(rows):
    if pattern_type == "triangle":
        print(char * (i + 1))
    elif pattern_type == "rectangle":
        print(char * rows)
    elif pattern_type == "diamond":
        spaces = abs(rows // 2 - i)
        stars = rows - 2 * spaces
        print(" " * spaces + char * stars)
