# A website requires a user to input username and password to register.
# Write a program to check the validity of password given by user.
# Following are the criteria for checking password:
# 1. At least 1 letter between [a-z]
# 2. At least 1 number between [0-9]
# 3. At least 1 letter between [A-Z]
# 4. At least 1 character from [$#@]
# 5. Minimum length of transaction password: 6
# 6. Maximum length of transaction password: 12

print("Enter password")
password = input(">>> ")


def check_lower_case(password):
    contains_lower = False
    for string in password:
        if string.islower():
            contains_lower = True
            break
    return contains_lower


def check_upper_case(password):
    contains_upper = False
    for string in password:
        if string.isupper():
            contains_upper = True
            break
    return contains_upper


def check_digit(password):
    contains_digit = False
    for string in password:
        if string.isnumeric():
            contains_digit = True
            break
    return contains_digit


def check_special_characters(password):
    contains_special_chars = False
    special_chars = "$#@"
    for string in password:
        if string in special_chars:
            contains_special_chars = True
            break
    return contains_special_chars


def validate_length(password):
    length = len(password)
    return length >= 6 and length <= 12


def validate_password(password):
    return check_lower_case(password) and check_upper_case(password) and check_digit(password) and check_special_characters(password) and validate_length(password)


if validate_password(password):
    print("Password is valid.")
else:
    print("Password is not valid.")
