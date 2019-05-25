# 1. Extract data from the givenSalaryGender CSV file and store the data
# from each column in a separate NumPy array

import numpy as np
import pandas as pd

df_salary_gender = pd.read_csv("SalaryGender.csv")

salary = np.array(df_salary_gender["Salary"])
gender = np.array(df_salary_gender["Gender"])
age = np.array(df_salary_gender["Age"])
phd = np.array(df_salary_gender["PhD"])
