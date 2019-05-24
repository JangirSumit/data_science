import pandas as pd
import matplotlib as plt

df = pd.read_csv("BigMartSalesData.csv")

df_grouped_year = df.query("Year == 2011").filter(
    ["Month", "Amount"]).groupby(["Month"], as_index=False).sum()

# Plot Total Sales Per Month for Year 2011.
x = df_grouped_year["Month"]
y = df_grouped_year["Amount"]

plt.plot(x, y)
plt.xlabel("Month")
plt.ylabel("Total Sales")
plt.title("Month vs sales")
plt.grid()
plt.show()


# How the total sales have increased over months in Year 2011.
# Total sales almost increased till 11th month but decreased in 12th month


# Which month has lowest Sales?
# By seeing graph we can directly say that the lowest sales in 2nd month
