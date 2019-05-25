# 4. Calculate the total number of people who have a PhD degreefrom SalaryGender CSV file.

import pandas as pd

csv_data = pd.read_csv('SalaryGender.csv')

# filter data from rows
people_phd = csv_data.query("PhD == 1")

print("Total number of people with PhD degree" + str(people_phd.shape[0]))
