# User input for two numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Equality (==) and Inequality (!=)
if num1 == num2:
    print(f"{num1} is equal to {num2}")
else:
    print(f"{num1} is not equal to {num2}")

# Greater Than (>) and Less Than (<)
if num1 > num2:
    print(f"{num1} is greater than {num2}")
elif num1 < num2:  # Notice the "elif" for an alternative condition
    print(f"{num1} is less than {num2}")

# Greater Than or Equal To (>=) and Less Than or Equal To (<=)
if num1 >= num2:
    print(f"{num1} is greater than or equal to {num2}")
if num1 <= num2:
    print(f"{num1} is less than or equal to {num2}")
