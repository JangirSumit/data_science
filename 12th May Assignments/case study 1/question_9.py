# 9. Create a random vector of size 30 and find the mean value.

import math

np_array = np.arange(0,30)

x,y = 0,0

while x*y != 30:
    x = random.randint(1,31)
    y = random.randint(1,31)

np_array = np_array.reshape(x,y)

print(np_array)

print("Mean of Above Array is " + str(np_array.mean()))