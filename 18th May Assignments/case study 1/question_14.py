# 14. Create a randommatrix and Compute a matrix rank

import numpy as np

np_array = np.random.random(16).reshape(2, 2, 2, 2)
print(np_array)

array = np.array([4, 2, 7, 1])
temp = array.argsort()
ranks = np.empty_like(temp)
ranks[temp] = np.arange(len(array))

print(ranks)
