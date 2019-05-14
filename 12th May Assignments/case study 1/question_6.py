# 6. Create a numpyarray [[0, 1, 2],[ 3, 4, 5],[ 6, 7, 8],[ 9,10, 11]]) and filter the elements greater than 5.

import numpy as np

np_array = np.array([[0, 1, 2],[ 3, 4, 5],[ 6, 7, 8],[ 9,10, 11]])
arr_gt_5 = np_array[np_array > 5]

print(arr_gt_5)