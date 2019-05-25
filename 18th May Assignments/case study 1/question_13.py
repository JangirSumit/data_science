# 13. Create a random array and swap two rows of an array.

import numpy as np

np_array = np.random.random((3, 3))

print(np_array)

np_array[[0, 1]] = np_array[[1, 0]]

print(np_array)
