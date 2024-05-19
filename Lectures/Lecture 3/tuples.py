import math

# Task 1: Basic Tuple Creation and Access
favorite_foods = ("pizza", "sushi", "tacos")
print(favorite_foods[0])  # Output: pizza

# Task 2: Tuple Unpacking
person = ("Alice", 30)
name, age = person
print(f"{name} is {age} years old.")  # Output: Alice is 30 years old.

# Task 3: Tuple Immutability (Demonstrating an error)
# favorite_foods[1] = "burger"  # This will raise a TypeError

# Task 4: Tuple Operations
fruits = ("apple", "banana")
more_fruits = ("orange", "apple", "grape")
all_fruits = fruits + more_fruits
apple_count = all_fruits.count("apple")
print(apple_count)  # Output: 2

# Task 5: Finding Items in a Tuple
if "banana" in all_fruits:
    print("Banana is in the tuple!")

# Task 6: Tuple Conversion
fruits_list = list(all_fruits)
print(fruits_list)  # Output: ['apple', 'banana', 'orange', 'apple', 'grape']

# Task 7: Nested Tuples
book = ("The Hitchhiker's Guide to the Galaxy", "Douglas Adams", 1979)

# Task 8: Tuple Slicing
first_two_fruits = all_fruits[:2]
print(first_two_fruits)  # Output: ('apple', 'banana')

# Task 9: Challenge: Tuple Unpacking and Processing
coordinates = (3, 4, 12)
x, y, z = coordinates
distance = math.sqrt(x ** 2 + y ** 2 + z ** 2)
print(f"Distance from origin: {distance}")  # Output: Distance from origin: 13.0
