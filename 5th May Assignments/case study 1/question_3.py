# 3. Write a program, which will find all the numbers between 1000 and 3000
# (both included) such that each digit of a number is an even number.
# The numbers obtained should be printed in a comma separated sequence on a single line.

list = []

for number in range(1000, 3001):
    even_counts = 0
    for num in str(number):
        if int(num) % 2 == 0:
            even_counts += 1
        else:
            break

    if even_counts == len(str(number)):
        list.append(str(number))

print(",".join(list))
