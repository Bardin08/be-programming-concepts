from functools import reduce

NUMBERS = range(1, 16)  # [1, 2, 3, ..., 15]
RANDOM_STRINGS = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape", "honeydew", "kiwi", "lemon"]

# Useful Functions:

# filter() - Filter elements from a list based on a condition
print("Filtering words that start with 'ba'")
prefix = "ba"
filtered_words = list(filter(lambda w: w.startswith(prefix), RANDOM_STRINGS))
print(filtered_words)

# map() - Apply a function to each element of a list
print("Capitalizing filtered words")
filtered_words = list(map(str.capitalize, filtered_words))
print(filtered_words)

# sorted() - Sort elements of a list
print("Sorting filtered words in reverse order")
filtered_words = list(sorted(filtered_words, reverse=True))
print(filtered_words)

# reduce() - Reduce elements of a list to a single value
print("Summing numbers from 1 to 15")
sum_1 = reduce(lambda x, y: x + y, NUMBERS)
print(sum_1)

# zip() - Combine elements of two lists
print("Zipping two lists")
list_1 = range(1, 11)
list_2 = range(20, 31)
zipped_lists = zip(list_1, list_2)
print(list(zipped_lists))

# enumerate() - Enumerate elements of a list
print("Enumerating random strings")
for index, value in enumerate(RANDOM_STRINGS):
    print(index, value)

# reversed() - Reverse the elements of a list
print("Reversing random strings")
for value in reversed(RANDOM_STRINGS):
    print(value)

# all() - Check if all elements of a list are True
print("Checking if all words have the letter 'a'")
has_letter_a = map(lambda w: 'a' in w, RANDOM_STRINGS)
passed = all(has_letter_a)
print(passed)

# any() - Check if any element of a list is True
print("Checking if any words have the letter 'a'")
passed = any(has_letter_a)
print(passed)

# sum() - Sum elements of a list
print("Summing numbers from 1 to 15")
sum_2 = sum(NUMBERS)
print(sum_2)

# max() - Find the maximum element of a list
print("Finding the maximum number in the list")
max_number = max(NUMBERS)
print(max_number)

# min() - Find the minimum element of a list
print("Finding the minimum number in the list")
min_number = min(NUMBERS)
print(min_number)

# len() - Find the length of a list
print("Finding the length of the list")
length = len(RANDOM_STRINGS)
print(length)

# list() - Convert an iterable to a list
# tuple() - Convert an iterable to a tuple
# set() - Convert an iterable to a set
