# Task 1: Basic Set Creation and Adding Elements
unique_numbers = {1, 2, 3}
unique_numbers.add(4)
unique_numbers.add(2)  # No effect, as 2 is already in the set
print(unique_numbers)  # Output: {1, 2, 3, 4} (order may vary)

# Task 2: Set Operations
colors = {"red", "green", "blue"}
more_colors = {"blue", "yellow", "orange"}

union_colors = colors | more_colors  # Union
print(union_colors)  # Output: {'orange', 'blue', 'green', 'red', 'yellow'}

intersection_colors = colors & more_colors  # Intersection
print(intersection_colors)  # Output: {'blue'}

difference_colors = colors - more_colors  # Difference
print(difference_colors)  # Output: {'red', 'green'}

# Task 3: Membership Testing
print("blue" in colors)  # Output: True
print("purple" in colors)  # Output: False

# Task 4: Removing Items
unique_numbers.remove(2)  # Removes 2 from the set
# unique_numbers.remove(5)  # Raises a KeyError since 5 is not in the set

unique_numbers.discard(3)  # Removes 3
unique_numbers.discard(5)  # No error, even though 5 is not in the set
print(unique_numbers)  # Output: {1, 4}

# Task 5: Set Comprehension
even_numbers = {x for x in range(1, 11) if x % 2 == 0}
print(even_numbers)  # Output: {2, 4, 6, 8, 10}

# Task 6: Challenge: Finding Unique Characters in a String
text = "abracadabra"
unique_chars = set(text)
print(unique_chars)  # Output: {'a', 'r', 'b', 'c', 'd'}
