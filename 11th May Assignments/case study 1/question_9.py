# Write a program which takes 2 digits, X,Y as input and generates a 2-dimensional array.
# The element value in the i-th row and j-th column of the array should be i*j.
# Note: i=0,1.., X-1; j=0,1,¡-Y-1.
# Example:Suppose the following inputs are given to the program:
# 3,5
# Then, the output of the program should be:
# [[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]]

print("Enter the X,Y")
XY = input(">>> ").split(",")

list_array = []

X = int(XY[0].strip())
Y = int(XY[1].strip())

for x in range(X):
    list_temp = []
    for y in range(Y):
        list_temp.append(y*x)
    list_array.append(list_temp)

print(list_array)
