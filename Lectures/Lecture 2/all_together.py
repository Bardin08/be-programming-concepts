import random  # For generating random numbers

# Data Setup
name = "Alice"
age = 30
temperature = 22.5
is_member = True
discount_percentage = 10 if is_member else 0

# Numerical Calculations
bill_amount = random.uniform(50, 200)
discount_amount = bill_amount * (discount_percentage / 100)
final_bill = bill_amount - discount_amount

# String Formatting
greeting = f"Hello, {name}! You are {age} years old."
weather_message = f"The temperature is {temperature:.1f}°C. {'It\'s a nice day!' if temperature > 20 else 'A bit chilly!'}"
bill_summary = f"Your total bill is ${final_bill:.2f} (after a ${discount_amount:.2f} discount)."

# Boolean Logic and Decisions
if is_member:
    additional_message = "Thank you for being a member! You saved money today."
else:
    additional_message = "Consider becoming a member to enjoy discounts!"

# Output to the User
print(greeting)
print(weather_message)
print(bill_summary)
print(additional_message)

# More complex condition
# (18 <= age <= 65) and (15 < temperature < 30):
if (age >= 18 and age <= 65) and (temperature > 15 and temperature < 30):
    suggestion = "It's a great day for outdoor activities!"
else:
    suggestion = "Perhaps stay indoors or choose activities suitable for the weather."

print(suggestion)
