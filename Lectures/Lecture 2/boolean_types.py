is_raining = True
is_sunny = False

# Using Boolean operators
if is_raining and is_sunny:
    print("It's a rainbow!")
elif is_raining or is_sunny:
    if is_raining:
        print("Bring an umbrella!")
    else:
        print("Wear sunscreen!")
else:
    print("Perfect weather for a walk!")

# Truthiness and Falseness
empty_list = []
non_empty_string = "Hello"
zero = 0

if empty_list:
    print("Empty list is truthy!")  # This won't print
if non_empty_string:
    print("Non-empty string is truthy!")
if zero:
    print("Zero is truthy!")  # This won't print

# Comparison and Membership
temperature = 15
if temperature > 25:
    print("It's hot!")
elif 10 <= temperature <= 20:
    print("It's mild.")
else:
    print("It's cold!")

activities = ["hiking", "swimming", "reading"]
if "swimming" in activities:
    print("Let's go swimming!")
else:
    print("Maybe another activity?")

# Identity (checking if variables refer to the same object)
a = [1, 2, 3]
b = a
c = [1, 2, 3]
if a is b:
    print("a and b are the same object")
if a is not c:
    print("a and c are different objects, even though they have the same content")
