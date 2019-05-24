# 3. Print the names of the top five movies with the costliest budgets.

import pandas as pd

df = pd.read_csv('HollywoodMovies.csv')

sorted_df = df.sort_values("Budget", ascending=False)

sorted_df = sorted_df[sorted_df["Budget"] > 0]  # removing nan values

print(sorted_df.head(5))
