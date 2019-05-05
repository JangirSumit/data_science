# 1. Write a program which will find factors of given number and find whether the factor is even or odd.

print("Enter a number")
number = int(input(">>> "))

################################ Prime Factors ####################################

# list = []
# factor = 2
# copy_number = number

# while factor != number:
#     if copy_number % factor == 0:
#         list.append(str(factor))
#         copy_number /= factor
#     else:
#         factor += 1

# print("Prime factrors are :  " + " * ".join(list))

print("All factors of number is\n")
for num in range(1, number + 1):
    if number % num == 0:
        if num % 2 == 0:
            print(f"{num} - even")
        else:
            print(f"{num} - odd")
