# 12. Write a program that accepts a sequence of whitespace separated words as input and
# prints   the   words   after   removing   all   duplicate   words   and
# sorting   them alphanumerically.
# Suppose the following input is supplied to the program:
# hello world and practice makes perfect and hello world again
# Then, the output should be:
# again and hello makes perfect practice world

print("Enter string")
string = input(">>> ")

string_list = string.split(" ")
unique_words = list(set(string_list))
unique_words.sort()

print(" ".join(unique_words))
