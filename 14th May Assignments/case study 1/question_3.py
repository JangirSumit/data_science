# 3. Use SalaryGender CSV file. 
# Store the “Age” and “PhD” columns in one DataFrame and delete the data of all people who don’t have a PhD

# https://medium.com/dunder-data/selecting-subsets-of-data-in-pandas-6fcd0170be9c

# 4. Calculate the total number of people who have a PhD degreefrom SalaryGender CSV file.

import numpy as np

my_data = np.genfromtxt('SalaryGender.csv', delimiter=',', skip_header=1)

people_phd = [data[2:3] for data in csv_data]

print("Total number of people who have a PhD degree " + str(len(people_phd)))