# 2. Find:
# 1. The number of men with a PhD
# 2. The number of women with a PhD

import numpy as np
import pandas as pd

df_salary_gender = pd.read_csv("SalaryGender.csv")

mens_phd = df_salary_gender.query("Gender == 1 and PhD == 1")
womens_phd = df_salary_gender.query("Gender == 0 and PhD == 1")

print("The number of men with a PhD " + str(len(mens_phd)))
print("The number of women with a PhD " + str(len(womens_phd)))
