# 8. Create  a  10x10  array  with  random  values  and  find  the  minimum  and  maximum values.

import random
import numpy as np

list = []

for _ in range(100):
    list.append(random.randint(1,1000))

np_array = np.array(list)

print("Max value " + str(max(np_array)))
print("Min value " + str(min(np_array)))