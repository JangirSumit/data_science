# 13. Write  a  program  which  accepts  a  sequence  of  comma  separated  4  digit
# binary numbers  as  its  input  and  then  check  whether  they  are  divisible  by  5  or  not.
# The numbers that are divisible by 5 are to be printed in a comma separated sequence.
# Example:
# 0100,0011,1010,1001
# Then the output should be:
# 1010

print("Enter comma seperated Binary numbers")
string = input(">>> ")

binary_list = string.split(",")
result_list = [bin_number for bin_number in binary_list if int(
    bin_number, 2) % 5 == 0]

result = ",".join(result_list)

print(result)
