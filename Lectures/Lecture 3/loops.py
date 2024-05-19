# Task 1: Basic for loop over a list
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)  # Output: apple banana cherry

# Task 2: Loop with range() function
for i in range(5): #range(start, stop, step)
    print(i)  # Output: 0 1 2 3 4

# Task 3: Looping over characters in a string
message = "Hello, world!"
for char in message:
    print(char)  # Output: H e l l o ,   w o r l d !

# Task 4: while loop with a counter
count = 0
while count < 5:
    print(count)  # Output: 0 1 2 3 4
    count += 1

# Task 5: while loop with a condition
number = 10
while number > 0:
    print(number)
    number -= 2  # Output: 10 8 6 4 2

# Task 6: Nested loops
for i in range(3):
    for j in range(2):
        print(f"({i}, {j})")
        # Output: (0, 0) (0, 1) (1, 0) (1, 1) (2, 0) (2, 1)

# Task 7: break and continue statements
for num in range(10):
    if num == 3:
        continue  # Skip 3
    if num == 7:
        break     # Exit the loop
    print(num)  # Output: 0 1 2 4 5 6

# Task 8: Looping with enumerate() for index and value
fruits = ["apple", "banana", "cherry"]
for index, fruit in enumerate(fruits):
    print(f"{index}: {fruit}")
    # Output: 0: apple
    #         1: banana
    #         2: cherry

# Task 9: Challenge: Calculate factorial using a for loop
number = 5
factorial = 1
for i in range(1, number + 1):
    factorial *= i
print(f"The factorial of {number} is {factorial}")  # Output: The factorial of 5 is 120

# Task 10: Challenge: Print a triangle pattern
for i in range(1, 6):
    print("*" * i)
# Output:
# *
# **
# ***
# ****
# *****
