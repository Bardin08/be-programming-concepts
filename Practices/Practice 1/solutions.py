# 1. Basic Arithmetic:
number1 = int(input("First number: "))
number2 = int(input("Second number: "))

addition = number1 + number2
subtraction = number1 - number2
multiplication = number1 * number2
division = number1 / number2
modulo = number1 % number2

print(f"{addition} (addition), {subtraction} (subtraction), {multiplication} (multiplication), "
      f"{division} (division), {modulo} (modulo)")

# -- Option 2 --
print(f"{addition} (addition),", end=" ")
print(f"{subtraction} (subtraction),", end=" ")
print(f"{multiplication} (multiplication),", end=" ")
print(f"{division} (division),", end=" ")
print(f"{modulo} (modulo)")

#  2. Temperature Conversion:

celsius_input = float(input("Specify a temperature in Celsius: "))
celsius_to_fahrenheit = (celsius_input * 9 / 5) + 32

print(celsius_to_fahrenheit)

# 3. String Manipulation:

input_string = input("Write something here: ")

print(len(input_string))
print(input_string[0])
print(input_string[-1])
print(input_string[::-1])  # or input_string.reverse()

# 4. Even or Odd:

number_input = int(input("Specify integer: "))
if number_input % 2 == 0:
    even_or_odd = "Even"
else:
    even_or_odd = "Odd"

print(even_or_odd)

# One row example:
# even_or_odd = "Even" if number_input % 2 == 0 else "Odd"

# 5. Simple Interest Calculation:

time_period = int(input("Specify time period in years: "))
principal = int(input("Specify principal amount: "))
rate_of_interest = int(input("Specify rate of interest: "))

simple_interest = (time_period * rate_of_interest * principal) / 100
print(simple_interest)

# 6. Area of a Triangle:

base = float(input("Base: "))
height = float(input("Height: "))

area = 0.5 * base * height
print(area)

# 7. BMI Calculator:

weight = float(input("Enter weight (kg): "))
height = float(input("Enter height (m): "))

bmi_results = round(weight / (height ** 2), 2)
print(bmi_results)

# 8. Grade Calculator:

first_grade = float(input("First grade: "))
second_grade = float(input("Second grade: "))
third_grade = float(input("Third grade: "))

sum_of_grade = first_grade + second_grade + third_grade
grades_avg = round(sum_of_grade / 3)

if grades_avg >= 90:
    mark = 'A'
elif grades_avg >= 80:
    mark = 'B'
elif grades_avg >= 70:
    mark = 'C'
elif grades_avg >= 60:
    mark = 'D'
else:
    mark = 'F'

print(f"Avg: {grades_avg}, Mark: {mark}")

# 9. Largest of Three Numbers:

first_grade = float(input("First grade: "))
second_grade = float(input("Second grade: "))
third_grade = float(input("Third grade: "))

if first_grade >= second_grade and first_grade >= third_grade:
    largest = first_grade
elif second_grade >= first_grade and second_grade >= third_grade:
    largest = second_grade
else:
    largest = third_grade

print("The largest grade is: ", largest)

# 10. Swapping Variables:

a = input("First value: ")
b = input("Second value: ")

temp = a
a = b
b = temp

# OR:
# a, b = b, a

print(f'a = {a}, b = {b}')
