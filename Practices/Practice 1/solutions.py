# Solutions will be added on the May 17, 2024.

# 1. Basic Arithmetic:
# number1 = int(input("First number: "))
# number2 = int(input("Second number: "))
#
# print(f"Add: {number1 + number2}")
# print(f"Sub: {number1 - number2}")
# print(f"Mul: {number1 * number2}")
# print(f"Div: {number1 / number2}")
# print(f"Mod: {number1 % number2}")

#  2. Temperature Conversion:

# celsius_input = float(input("Specify a temperature in Celsius: "))
# celsius_to_fahrenheit = (celsius_input * 9/5) + 32
#
# print(celsius_to_fahrenheit)

# 3. String Manipulation:

# input_string = input("Write something here: ")
#
# print(len(input_string))
# print(input_string[0])
# print(input_string[-1])
# print(input_string[::-1]) # or input_string.reverse()

# 4. Even or Odd:

# number_input = int(input("Specify integer: "))
# if number_input % 2 == 0:
#     even_or_odd = "Even"
# else:
#     even_or_odd = "Odd"
#
# print(even_or_odd)
# One row example:
# even_or_odd = "Even" if number_input % 2 == 0 else "Odd"

# 5. Simple Interest Calculation:

# time_period = int(input("Specify time period in years: "))
# principal = int(input("Specify principal amount: "))
# rate_of_interest = int(input("Specify rate of interest: "))
#
# simple_interest = (time_period * rate_of_interest * principal) / 100
# print(simple_interest)

# 6. Area of a Triangle:

# base = float(input("Base: "))
# height = float(input("Height: "))
#
# area = 0.5 * base * height
# print(area)

# 7. BMI Calculator:

# weight = float(input("Enter weight (kg): "))
# height = float(input("Enter height (m): "))
#
# bmi_results = round(weight / (height ** 2), 2)
# print(bmi_results)

# 8. Grade Calculator:

# grade_list = input("Enter three grades separated by spaces: ").split()
#
# grade_list = list(map(int, grade_list))
# # OR
# # for i in range(0, len(grade_list)):
# #     grade_list[i] = int(grade_list[i])
#
# grades_avg = round(sum(grade_list) / 3)
#
# if grades_avg >= 90:
#     mark = 'A'
# elif grades_avg >= 80:
#     mark = 'B'
# elif grades_avg >= 70:
#     mark = 'C'
# elif grades_avg >= 60:
#     mark = 'D'
# else:
#     mark = 'F'
#
# print(f"Avg: {grades_avg}, Mark: {mark}")

# 9. Largest of Three Numbers:

# numbers_list = input("Enter three numbers: ").split()
# numbers_list = list(map(int, numbers_list))
# numbers_list.sort(reverse=True)
# print(numbers_list[0])

# 10. Swapping Variables:

# a = input("First value: ")
# b = input("Second value: ")
#
# temp = a
# a = b
# b = temp
# # OR:
# # a, b = b, a
#
# print(f'a = {a}, b = {b}')


