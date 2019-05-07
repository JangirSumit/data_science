# 12. Write  a  program  to  compute  1/2+2/3+3/4+...+n/n+1  with  a  given  n  input  by console (n>0).
# Example:
# If the following n is given as input to the program:
# 5
# Then, the output of the program should be:
# 3.55

print("Enter a number")
number = int(input(">>> "))

total = 0.0
for num in range(1, number+1):
    total += (num)/(num+1)

print(total)
