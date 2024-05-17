# 1. Number Comparison:
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

if num1 > num2:
    print("The first number is larger.")
elif num2 > num1:
    print("The second number is larger.")
else:
    print("The numbers are equal.")

# 2. Leap Year Checker:
year = int(input("Enter a year: "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")

# 3. Vowel or Consonant:
char = input("Enter a character: ").lower()

if char in "aeiou":
    print(f"{char} is a vowel.")
else:
    print(f"{char} is a consonant.")

# 4. Quadrant Identifier:
x = float(input("Enter the x-coordinate: "))
y = float(input("Enter the y-coordinate: "))

if x > 0 and y > 0:
    print("Quadrant I")
elif x < 0 < y:
    print("Quadrant II")
elif x < 0 and y < 0:
    print("Quadrant III")
elif x > 0 > y:
    print("Quadrant IV")
elif x == 0 and y != 0:
    print("On the y-axis")
elif x != 0 and y == 0:
    print("On the x-axis")
else:
    print("At the origin")

# 5. Password Strength Checker:
password = input("Enter a password: ")

has_length = len(password) >= 8
is_uppercase = any(c.isupper() for c in password)
is_lowercase = any(c.islower() for c in password)
is_digit = any(c.isnumeric() for c in password)

if has_length and is_lowercase and is_uppercase and is_digit:
    print("Strong password")
else:
    print("Weak password")
