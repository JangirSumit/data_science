# 7. Write a program which can compute the factorial of a given numbers. Use recursion to find it.
# Hint: Suppose the following input is supplied to the program:
# 8
# Then, the output should be:
# 403208.


def factorial(number):
    if number == 0:
        return 1
    else:
        return number*factorial(number-1)


print("Please enter a number")
number = int(input(">>> "))

print(f"Factorial of given number is {factorial(number)}")
