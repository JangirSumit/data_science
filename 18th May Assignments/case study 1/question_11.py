# 11. Create a random array of 3 rows and 3 columns and sort it according to 1stcolumn,
# 2ndcolumn or 3rdcolumn.

import numpy as np

np_array = np.random.random(9).reshape(3, 3)
print(np_array)

np_new = np.sort(np_array, axis=0)
print(np_new)
