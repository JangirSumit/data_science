# 10. By using list comprehension, please write a program to print the list after removing the 0th,4th,5th numbers in [12,24,35,70,88,120,155].

given_list = [12,24,35,70,88,120,155]

# removing index from highest to lowest otherwise index will be changed
del given_list[5]
del given_list[4]
del given_list[0]

print(given_list)
