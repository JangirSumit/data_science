# 8. Create  a  10x10  array  with  random  values  and  find  the  minimum  and  maximum values.

import numpy as np

np_array = np.random.random((10, 10))

print(np_array)

print("Max value " + str(np_array.max()))
print("Min value " + str(np_array.min()))
