# 3. Create csv file from the data file available in LMS which goes by the name ‘M4_assign_dataset’and read this file into apandas data frame

import pandas as pd

df_data_file = pd.read_csv("data_file.txt")
df_data_file.to_csv("data_file.csv")