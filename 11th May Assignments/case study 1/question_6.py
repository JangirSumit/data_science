# 6. Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5,
# between 2000 and 3200 (both included).
# The numbers obtained should be printed in a comma-separated sequence on a single line.


result_list = [str(number) for number in range(
    2000, 3201) if (not number % 7) and number % 5]

print(",".join(result_list))
