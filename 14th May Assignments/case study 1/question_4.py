# 4. Calculate the total number of people who have a PhD degreefrom SalaryGender CSV file.

import numpy as np

my_data = np.genfromtxt('SalaryGender.csv', delimiter=',', skip_header=1)

people_age_phd = [data[2:] for data in csv_data]

print(people_age_phd)

print()

print("Total number of people who have a PhD degree " + str(len(people_phd)))