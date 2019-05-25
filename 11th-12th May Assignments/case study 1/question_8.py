# 8. Write a program that calculates and prints the value according to the given formula:
# Q = Square root of [(2 * C * D)/H]
# Following are the fixed values of C and H: C is 50. H is 30.
# D  is  the  variable  whose  values  should  be  input  to  your  program  in  a  comma-separated sequence.
#
# Example:Let  us  assume  the  following  comma  separated  input  sequence  is  given  to  the program:100,150,180
# The output of the program should be:18,22,249.

import math


def get_formula_value(D):
    C = 50
    H = 30
    return int(math.sqrt(((2*C*D)/H)))


print("Enter numbers")
numbers = input(">>> ")

numbers_list = [int(number) for number in numbers.split(",")]

for number in numbers_list:
    print(get_formula_value(number))
