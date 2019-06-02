import pandas as pd


df = pd.read_csv("Practise\BostonHousing.csv")
# print(df.head())

# Selection
# print(df.loc[:, ["crim", "indus"]])
print(df.iloc[[0, 1], [0, 1]])
