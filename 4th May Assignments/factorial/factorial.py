print("****** Factorial Program ******")
print("Please enter a number")
number = int(input(">>> "))

result = 1

for num in range(2, number+1):
    result *= num

print("Factorial of given number is : " + str(result))
