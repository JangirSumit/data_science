import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df_prisoners = pd.read_csv("prisoners.csv")

# 1.Data Loading:
# a.Load the dataset “prisoners.csv” using pandas and display the first and last five rows in the dataset. 
print(df_prisoners.head())
print(df_prisoners.tail())

# b.Use describe method in pandas and find out the number of columns. Can you say something about those rows who have zero inmates?
print(df_prisoners.describe())


# 2.Data Manipulation:
# a.Create a new column -’total_benefitted’ that is a sum of inmates benefitted through all modes.
df_prisoners["total_benefitted"] = df_prisoners["No. of Inmates benefitted by Elementary Education"] + df_prisoners["No. of Inmates benefitted by Adult Education"] + df_prisoners["No. of Inmates benefitted by Higher Education"] + df_prisoners["No. of Inmates benefitted by Computer Course"]
df_prisoners.head()

# b.Create a new row -“totals” that is the sum of all inmates benefitted through each mode across all states.
df_prisoners = df_prisoners.append(df_prisoners.sum(), ignore_index=True)
df_prisoners.at[35, "STATE/UT"] = "totals"
df_prisoners.at[35, "YEAR"] = ""

print(df_prisoners.head())


# 3.Plotting:
# a.Make a bar plot with each state name on the x -axis and their total benefitted inmates astheir bar heights. 
# Which state has the maximum number of beneficiaries?
x = df_prisoners["STATE/UT"]
y = df_prisoners["total_benefitted"]

plt.bar(x,y)
plt.setp(plt.gca().get_xticklabels(), rotation=90,horizontalalignment='right') 
plt.title("STATE/UT vs Total_inmates_benefitted")
plt.xlabel("STATE/UT")
plt.ylabel("Total_inmates_benefitted")
plt.show()

# b.Make a pie chart that depicts the ratio among different modes of benefits.
labels = df_prisoners["STATE/UT"]
values = df_prisoners["total_benefitted"]

plt.pie(values, labels = labels, autopct='%1.1f%%', shadow=True)
plt.title("STATE/UT vs Total_inmates_benefitted")
plt.show()