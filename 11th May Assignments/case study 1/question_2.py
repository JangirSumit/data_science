# 2. Data of XYZ company is stored in sorted list. Write a program for searching specific data from that list.
# Hint: Use if/elif to deal with conditions.

string = input("Enter list of items (comma seperated)>>> ")
find_ele = input("Enter the elements which needs to find>>> ")

list_eles = str(string).split(",")

if find_ele in list_eles:
    print(f"{find_ele} is present in given list at position {list_eles.index(find_ele)+1}")
else:
    print(f"{find_ele} is not present in given list")
