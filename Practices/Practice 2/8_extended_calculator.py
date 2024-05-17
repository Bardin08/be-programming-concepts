num1 = float(input("Enter the first number: "))
op = input("Enter operator (+, -, *, /): ")
num2 = float(input("Enter the second number: "))

if op == "+":
    print(num1 + num2)
elif op == "-":
    print(num1 - num2)
elif op == "*":
    print(num1 * num2)
elif op == "/":
    if num2 == 0:
        print("Cannot divide by zero")
    else:
        print(num1 / num2)

# Add more operations like exponentiation, modulo, etc.
