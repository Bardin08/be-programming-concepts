import math

# Floating-Point Methods
pi = 3.14159
print(f"Pi is an integer? {pi.is_integer()}")  # False
numerator, denominator = pi.as_integer_ratio()
print(f"Pi as a ratio: {numerator}/{denominator}")  # 353711/112831

# Integer Methods
x = 256
y = 256

# Common Operations & Functions
result = x / y  # Division
print(f"Division result: {result}")  # 1.0

floor_result = x // y  # Floor division
print(f"Floor division: {floor_result}")  # 1

remainder = x % y  # Modulo
print(f"Remainder: {remainder}")  # 0

absolute_value = abs(-result)
print(f"Absolute value: {absolute_value}")  # 1.0

rounded = round(pi, 2)
print(f"Rounded pi: {rounded}")  # 3.14

square_root = math.sqrt(x)
print(f"Square root of 256: {square_root}")  # 16.0
