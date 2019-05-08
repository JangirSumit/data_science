# 11. Write a program that accepts sequence of lines as input and prints the lines
# after making all characters in the sentence capitalized.
# Suppose the following inputis supplied to the program:
# Hello world
# Practice makes perfect
# Then, the output should be:
# HELLO WORLD
# PRACTICE MAKES PERFECT

print("Enter strings")

while True:
    string = input("[Enter 1 to break]>>> ")
    if string == "1":
        break
    print(string.upper())
