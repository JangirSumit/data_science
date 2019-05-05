# 5. Please   write   a   program   which accepts  a   string   from   console
# and   print   the characters that have even indexes.
# Example: If the following string is given as input to the program:
# H1e2l3l4o5w6o7r8l9d
# Then, the output of the program should be:
# Helloworld

print("Enter string")
string = input(">>> ")

output_string = ""

for s in string:
    if string.index(s) % 2 == 0:
        output_string += s


print(output_string)
