# Task 1: Basic List Creation and Access
colors = ["red", "blue", "green", "yellow"]
print(colors[1])  # Output: blue

# Task 2: List Modification
colors.append("purple")
colors[0] = "orange"
print(colors)  # Output: ['orange', 'blue', 'green', 'yellow', 'purple']

# Task 3: List Slicing
middle_colors = colors[1:3]
print(middle_colors)  # Output: ['blue', 'green']

# Task 4: List Operations
numbers = [1, 2, 3]
combined = colors + numbers
total_length = len(combined)
print(total_length)  # Output: 8

# Task 5: Finding Items in a List
if "green" in colors:
    print("Green is in the list!")

# Task 6: Removing Items
colors.remove("yellow")
print(colors)  # Output: ['orange', 'blue', 'green', 'purple']

# Task 7: List Sorting
colors.sort()
print(colors)  # Output: ['blue', 'green', 'orange', 'purple']

# Task 8: List Comprehensions
squares = [x**2 for x in range(1, 6)]
print(squares)  # Output: [1, 4, 9, 16, 25]

# Task 9: Nested Lists
board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]

# Task 10: Challenge: List Filtering
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
even_numbers = [x for x in numbers if x % 2 == 0]
print(even_numbers)  # Output: [2, 4, 6, 8]
