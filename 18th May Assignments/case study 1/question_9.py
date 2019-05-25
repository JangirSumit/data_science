import numpy as np
import random

np_array = np.random.random(30)


x, y = 0, 0

while x*y != 30:
    x = random.randint(1, 31)
    y = random.randint(1, 31)

np_array = np_array.reshape(x, y)

print(np_array)

print("\nMean of Above Array is " + str(np_array.mean()))
