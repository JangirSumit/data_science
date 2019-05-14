# 7. Create a numpy array having NaN (Not a Number) and print it.
# array([ nan,   1.,   2.,  nan,   3.,   4.,   5.])
# Print the same array omitting all elements which are nan

import numpy as np

np_array = np.array([ np.NaN,   1.,   2.,  np.NaN,   3.,   4.,   5.])
print(np_array)

arr_without_nan = np_array[~np.isnan(np_array)] # use ~ for negation
print(arr_without_nan)