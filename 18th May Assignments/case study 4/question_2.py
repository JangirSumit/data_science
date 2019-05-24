import pandas as pd
import matplotlib as plt

df = pd.read_csv("BigMartSalesData.csv")

df_grouped_year = df.query("Year == 2011").filter(
    ["Month", "Amount"]).groupby(["Month"], as_index=False).sum()

# Plot Total Sales Per Month for Year 2011 as Bar Chart.
x = df_grouped_year["Month"]
y = df_grouped_year["Amount"]

plt.plot(x, y)
plt.xlabel("Month")
plt.ylabel("Total Sales")
plt.title("Month vs sales")
plt.grid()
plt.show()

# Is Bar Chart Better to visualize than Simple Plot?

# Line graphs are used to track changes over short and long periods of time.
# When smaller changes exist, line graphs are better to use than bar graphs.
# Line graphs can also be used to compare changes over the same period of time for more than one group.

# Bar graphs are used to compare things between different groups or to track changes over time.
# However, when trying to measure change over time, bar graphs are best when the changes are larger.
