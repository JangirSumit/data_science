# 2. Find:
# 1. The number of men with a PhD
# 2. The number of women with a PhD

import numpy as np

my_data = np.genfromtxt('SalaryGender.csv', delimiter=',', skip_header=1)

mens_phd = [data for data in csv_data if data[1] == 0 and data[3] == 1]
womens_phd = [data for data in csv_data if data[1] == 1  and data[3] == 1]

print("The number of men with a PhD " + str(len(mens_phd)))
print("The number of women with a PhD " + str(len(womens_phd)))