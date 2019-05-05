# 5. Design a code which will find the given number is Palindrome number or not.

print("Enter a Number")
string = input(">>> ")

temp = list(string)
temp.reverse()

if "".join(temp) == string:
    print("Number is Palindrome")
else:
    print("Number is not Palindrome")
