# 1. Extract data from the givenSalaryGender CSV file and store the data from each column in a separate NumPy array

import numpy as np

my_data = np.genfromtxt('SalaryGender.csv', delimiter=',', skip_header=1)

salary = csv_data[0:,0]
gender = csv_data[0:,1]
age = csv_data[0:,2]
phd = csv_data[0:,3]
print(phd)