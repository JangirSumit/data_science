# 1. Write a program which will find factors of given number and find whether the factor is even or odd.

print("Enter a number")
number = int(input(">>> "))

all_factors = []
list = []
factor = 2
copy_number = number

while factor != number:
    if copy_number % factor == 0:
        list.append(str(factor))
        copy_number /= factor
    else:
        factor += 1

print("Prime factrors are :  " + " * ".join(list))

for num in range(1, number + 1):
    if number % num == 0:
        all_factors.append(str(num))

print("All factrors are :  " + " , ".join(all_factors))
