numbers = [1, 3, 5, 7]

removed = numbers.pop()
print(removed)

# ----------------------------

a = 10
b = 20

t1 = (a, b)

a_index = t1.index(a)
b_index = t1.index(b)

t2 = t1[b_index], t1[a_index]  # (b, a)

# ----------------------------

numbers = [1, 2, 3, 4, 5]

for n in numbers:
    if n % 2 == 0:
        print(n)

for i, n in enumerate(numbers):
    if n % 2 == 0:
        print(i, ":", n)

[print(i, ":", n) for i, n in enumerate(numbers) if n % 2 == 0]
print([n for n in range(1, 8)])
