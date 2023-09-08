# Author: Patrick Thrower
# Student ID: T00620480
# Date: Sept 8, 2023
# Version: 1.0
# Description: A program that takes codes from a file checks codes for validity or if their restricted or not

valid_codes = []
invalid_codes = []
invalid_restricted_codes = []

def is_valid_code(input):  # Checks if the code is valid
    if (len(input) < 10):  # Checks if the code is 10 digits or longer
        return False
    if not (input[9].isupper()):  # Checks if the security digit is capitalized
        return False
    if not (input[3:7].isdigit()):  # Checks that the country code is digits
        return False
    return True

def is_restricted(input): # Checks if the security digit is "R" and that the code is over 2 in the thousands place of the country code
    if(input[9] == "R" and int(input[3]) >= 2):  
        return True
    return False

with open('Codes.txt', 'r') as file:  # Opens the Codes.txt file and reads input line by line
    product_codes = file.read().splitlines()

for code in product_codes:
    if is_valid_code(code) and not is_restricted(code):
        valid_codes.append(code)
    elif is_valid_code(code) and is_restricted(code):
        invalid_restricted_codes.append(code)
    elif not is_valid_code(code):
        invalid_codes.append(code)

print("Valid Code(s) are:")
for code in valid_codes:
    print(code)

print("\nInvalid Code(s) are:")
for code in invalid_codes:
    print(code)

print("\nInvalid Restricted Code(s) are:")
for code in invalid_restricted_codes:
    print(code)