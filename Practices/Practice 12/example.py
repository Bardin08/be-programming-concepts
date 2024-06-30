def is_number(n: str) -> bool:
    if n.count('-') == 1 and n[0] == '-':
        n = n[1:]

    if n.count('.') == 1:
        n = n.replace('.', '', 1)

    return n.isdigit()


print("Valid Number: ", is_number("123"))
print("Valid Number: ", is_number("-123"))
print("Valid Number: ", is_number("1.23"))
print("Valid Number: ", is_number("-1.23"))
print("InValid Number: ", is_number("-1.2.3"))
print("InValid Number: ", is_number("1.2.3"))
