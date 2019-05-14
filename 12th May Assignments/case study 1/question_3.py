# 3. Use SalaryGender CSV file.
# Store the “Age” and “PhD” columns in one DataFrame and delete the data of all people who don’t have a PhD

# https://medium.com/dunder-data/selecting-subsets-of-data-in-pandas-6fcd0170be9c

# 3. Use SalaryGender CSV file. Store the “Age” and “PhD” columns in one DataFrame and delete the data of all people who don’t have a PhD

import pandas as pd

csv_data = pd.read_csv('SalaryGender.csv')

# filter columns
age_phd = csv_data.filter(["Age", "PhD"])

# filter data from rows
people_age_phd = age_phd.query("PhD == 1")
# people_phd = csv_data[(csv_data.PhD == 1)] # another way

print(people_age_phd)