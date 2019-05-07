# 7. Please write a program which count and print the numbers of each character in a string input by console.
# Example: If the following string is given as input to the program:
# abcdefgabc
# Then, the output of the program should be:
# a,2
# c,2
# b,2
# e,1
# d,1
# g,1
# f,1

print("Enter string")
string = input(">>> ")

string_occ = {}

for s in string:
    if s not in string_occ.keys():
        string_occ[s] = string.count(s)
    

for key in string_occ.keys():
    print("{},{}".format(key, string_occ[key]))
