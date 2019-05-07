# 9. By using list comprehension, please write a program to print the list after removing the value 24 in [12,24,35,24,88,120,155].

given_list = [12,24,35,24,88,120,155]
item_to_remove = 24

# Method 1 - Traditional
########################

# while item_to_remove in given_list:
#     given_list.remove(24)
# 
# print(given_list)


# Method 2 - List comprehension
###############################

new_list = [item for item in given_list if item != item_to_remove]

print(new_list)