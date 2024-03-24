#create a loop to generate random password of a certain length. Password contains a mix of uppercase, lowercase and numbers


import random
import string

def generate_password(length):
    uppercase_letters = string.ascii_uppercase
    lowercase_letters = string.ascii_lowercase
    numbers = string.digits
    characters = uppercase_letters + lowercase_letters + numbers

    password = ''
    for _ in range(length):
        password += random.choice(characters)

    return password


length = 12
password = generate_password(length)
print(f"Generate password: {password}")



