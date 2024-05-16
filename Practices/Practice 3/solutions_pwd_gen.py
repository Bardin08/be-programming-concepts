import random
import string

SPECIALS = "!@#$%^&*()_+-=[]{}|<>?/~"

length = int(input("Enter desired password length: "))
include_lowercase = input("Include lowercase letters? (y/n): ").lower() == 'y'
include_uppercase = input("Include uppercase letters? (y/n): ").lower() == 'y'
include_digits = input("Include numbers? (y/n): ").lower() == 'y'
include_special = input("Include special characters? (y/n): ").lower() == 'y'

allowed = list(filter(lambda x: x is not None, [
    string.ascii_lowercase if include_lowercase else None,
    string.ascii_uppercase if include_uppercase else None,
    string.digits if include_digits else None,
    SPECIALS if include_special else None
]))

pwd = []
while len(pwd) < length:
    pwd.append(random.choice(random.choice(allowed)))

pwd_str = ''.join(pwd)
print("Generated password:", pwd_str)
