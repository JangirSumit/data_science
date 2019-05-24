# 1.You are given a dataset, which is present in the LMS, containing the number of hurricanes occurring in the 
# United States along the coast of the Atlantic. Load the data from the dataset into your program and plot a 
# Bar Graph of the data, taking the Year as the x-axis and the number of hurricanes occurring as the Y-axis.

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("Hurricanes.csv")

x = df["Year"]
y = df["Hurricanes"]

plt.bar(x,y)
plt.xlabel("Year")
plt.ylabel("Hurricanes")
plt.grid()
plt.title("Hurricanes vs Year")

plt.setp(plt.gca().get_xticklabels(), rotation=90, horizontalalignment='right') # Rotate Axis Labels

plt.show()