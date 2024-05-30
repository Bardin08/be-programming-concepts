def custom_filter(filter_rule, iterable):
    filtered = []
    for el in iterable:
        if filter_rule(el):
            filtered.append(el)

    return filtered


def custom_filter_v2(filter_rule, iterable):
    return [el for el in iterable if filter_rule(el)]


numbers = range(1, 11)
filtered_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(filtered_numbers)

for i in range(1, 60000):
    print("Custom filter: ", custom_filter(lambda x: x % 2 == 0, numbers))

print(f"Custom filter v2: {custom_filter_v2(lambda x: x % 2 == 0, numbers)}")

