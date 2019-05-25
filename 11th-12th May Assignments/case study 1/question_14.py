# 14. Write  a  program  that  accepts  a  sentence  and  calculate  the  number
# of  upper  case letters and lower case letters.
# Suppose the following input is supplied to the program:
# Hello world!
# Then, the output should be:
# UPPER CASE 1
# LOWER CASE 9

print("Enter string")
string = input(">>> ")

upper_case_letters = 0
lower_case_letters = 0

for s in string:
    if s.islower():
        lower_case_letters += 1
    elif s.isupper():
        upper_case_letters += 1

print(f"UPPER CASE {upper_case_letters}")
print(f"LOWER CASE {lower_case_letters}")
