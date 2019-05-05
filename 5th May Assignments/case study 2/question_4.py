# 4. Write a for loop that prints all elements of a list and their position in the list.

a = [4, 7, 3, 2, 5, 9]

for ele in a:
    print(f"{ele} - {a.index(ele) + 1}")
