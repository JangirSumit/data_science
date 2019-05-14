# 10. Create numpy array having elements 0 to 10 And negate all the elements between 3 and 9

import numpy as np

np_array = np.arange(0,10)

np_array = [(~d if (d>3 and d<9) else d) for d in np_array]

print(np_array)