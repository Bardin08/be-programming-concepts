import random
from functools import reduce


def add(a: int, b: int) -> int:
    print(a + b)
    return a + b


def add_v1(a, b):
    print(a + b)
    return a + b


def product(list_of_nums: list[int]) -> float:
    list_product = 1
    for n in list_of_nums:
        list_product *= n

    return list_product


# arg1 - nums to count
# arg2 - list of nums
def product_v1(*args):
    count = args[0]
    list_of_nums = args[1]

    list_product = 1
    for i, n in enumerate(list_of_nums):
        if i >= count:
            break

        list_product *= n

    return list_product


# arg1 - nums to count
# arg2 - list of nums
def product_v2(**kwargs):
    count = kwargs["count"]
    list_of_nums = kwargs["list"]

    list_product = 1
    for i, n in enumerate(list_of_nums):
        if i >= count:
            break

        list_product *= n

    return list_product


x = int(input("Enter x: "))
y = int(input("Enter y: "))

ab_sum = add(x, y)
ab_sum = add_v1(x, y)
print(f"Sum: {ab_sum}")

list_of_numbers = random.choices(range(1, 100), k=10)
print(list_of_numbers)
print("Product:", product_v1(2, list_of_numbers))
print("Product:", product_v2(count=2, list=list_of_numbers))

