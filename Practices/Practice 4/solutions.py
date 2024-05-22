# 1. Sum All Items in a List

int_list = [1, 2, 3, 4, 5]
list_sum = sum(int_list)
print(list_sum)


# 2. Multiply All Items in a List

inp_list = input("Enter integer elements separated by ' ': ")
inp_list = [int(el) for el in inp_list]

result = 1
for num in inp_list:
    result *= num

print(result)


# 3. Check if a List is Empty or Not

# 1st solution

new_list = []

if not new_list:
    print("The list is empty")
else:
    print("The list is not empty")

# # 2nd solution

if new_list == []:
    print("The list is empty")
else:
    print("The list is not empty")


# 4. Get the Smallest Number from a List

entered_list = input("Specify elements using ' ' between: ").split()
entered_list = [int(el) for el in entered_list]

entered_list.sort()
print(entered_list[0])


# 5. Get the Largest Number from a List

entered_list = input("Specify elements using ' ' between: ").split(" ")

while not entered_list:
    print("Invalid input!")
    entered_list = input("Specify elements using ' ' between: ").split(" ")

entered_list = [int(el) for el in entered_list]
entered_list.sort(reverse=True)
print(entered_list[0])


# 6. Remove Duplicates from a List

user_list = input("Specify elements using ' ' between them: ").split(" ")
without_duplicates_list = list(set(user_list))
print(without_duplicates_list)


# 7. Find Words Longer Than n

n = int(input("Enter min length of word: "))
words_list = ["apple", "monkey", "fish", "corresponding"]

result_list = []
for word in words_list:
    if len(word) > n:
        result_list.append(word)

print(result_list)


# 8. Check for Common Members in Two Lists

list1 = input("Enter the elements of the 1st, separated by spaces: ").split()
list2 = input("Enter the elements of the 2nd, separated by spaces: ").split()

common_found = False

for el in list1:
    if el in list2:
        common_found = True
        break

print(common_found)


# 9. Extend the First List

list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list2 = [1, "2", "3", "4"]

list1.extend(list2)
print(list1)

# 10. Multiple Integers into a Single Integer

multiple_integers = [123, 2022, 121, 30]

single_integer = ''
for el in multiple_integers:
    single_integer += str(el)

print(int(single_integer))