# 11. By using list comprehension, please write a program to print the list after removing delete numbers which are divisible by 5 and 7 in [12,24,35,70,88,120,155].

given_list = [12,24,35,70,88,120,155]
new_list = []

for item in given_list:
    if (item % 5 or item % 7):
        new_list.append(item)


print(new_list)