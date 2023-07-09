import random
import string
import pyperclip

uppercase_letters=[chr(i) for i in range(65,91)]
lowercase_letters=[chr(i) for i in range(97,123)]
numbers=[str(i) for i in range(9)]
special_characters=["!","@","#","$","%","^","&","*","(",")","+","=","-","_"]

def transform_choice(s):
    if s in {"Y","y"}:return True
    return False

def generate_password(length, include_uppercase, include_lowercase, include_numbers, include_special_chars):
    allowed = ["*"]

    if include_uppercase:
        allowed += uppercase_letters
    if include_lowercase:
        allowed += lowercase_letters
    if include_numbers:
        allowed += numbers
    if include_special_chars:
        allowed += special_characters

 
    password = ""
    for i in range(length):
        password += random.choice(allowed)

    return password



length = int(input("Enter the desired password length: "))
include_uppercase = transform_choice(input("Include uppercase letters? (Y/N): "))
include_lowercase = transform_choice(input("Include lowercase letters? (Y/N): "))
include_numbers = transform_choice(input("Include numbers? (Y/N): "))
include_special_chars = transform_choice(input("Include special characters? (Y/N): "))

generated_password = generate_password(length, include_uppercase, include_lowercase, include_numbers, include_special_chars)

pyperclip.copy(generated_password)

print("-"*60)
print("Your generated password is:", generated_password)
print("The password has been copied to your clipboard. Use Ctrl+V (or Command+V on Mac) to paste it.")

