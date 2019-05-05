# 4. Write a program that accepts a sentence and calculate the number of letters and digits.
# Suppose if the entered string is:
# Python0325
# Then the output will be:
# LETTERS: 6
# DIGITS: 4

print("Enter string")
string = input(">>> ")

letters = 0
digits = 0

for letter in string:
    if letter.isnumeric():
        digits += 1
    else:
        letters += 1

print(f"LETTERS: {letters}")
print(f"DIGITS: {digits}")
