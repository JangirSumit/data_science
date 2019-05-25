# 12. Create a four dimensions array get sum over the last two axis at once.

import numpy as np

np_array = np.random.random(16).reshape(2, 2, 2, 2)
print(np_array)
np.sum(np_array, axis=0)
