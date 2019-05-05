# 2. Write a code which accepts a sequence of words as input
# and prints the words in a sequence after sorting them alphabetically.

print("Enter sequence of words")
print("For example -\nMy name is Sumit\n")
words = input(">>> ")

temp = words.split(" ")
temp.sort()

sorted_string = " ".join(temp)

print("string after sorting is - \n")
print(f"{sorted_string}")
