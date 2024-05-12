# Temperature Converter
celsius = float(input("Enter temperature in Celsius: "))
fahrenheit = (celsius * 9 / 5) + 32
print(f"{celsius}°C is equal to {fahrenheit}°F")

# Odd or Even Checker
number = int(input("Enter a number: "))
if number % 2 == 0:
    print("Even")
else:
    print("Odd")

# Simple Calculator
num1 = float(input("Enter the first number: "))
op = input("Enter operator (+, -, *, /): ")
num2 = float(input("Enter the second number: "))

if op == "+":
    print(num1 + num2)
elif op == "-":
    print(num1 - num2)
elif op == "*":
    print(num1 * num2)
elif op == "/":
    if num2 == 0:
        print("Cannot divide by zero")
    else:
        print(num1 / num2)

# String Reverser
text = input("Enter a string: ")
reversed_text = text[::-1]
print(reversed_text)

# Word Counter
sentence = input("Enter a sentence: ")
words = sentence.split()
print(f"Number of words: {len(words)}")

# Password Generator
import random
import string

length = int(input("Enter password length: "))
chars = string.ascii_letters + string.digits + string.punctuation
password = ''.join(random.choice(chars) for _ in range(length))
print("Generated password:", password)

# Palindrome Checker
text = input("Enter a word or phrase: ")
cleaned_text = text.lower().replace(" ", "")
if cleaned_text == cleaned_text[::-1]:
    print("Palindrome!")
else:
    print("Not a palindrome.")

# File Word Frequency Counter
from collections import Counter

with open("your_file.txt", "r") as file:
    words = file.read().split()
    word_counts = Counter(words)
    print(word_counts)
