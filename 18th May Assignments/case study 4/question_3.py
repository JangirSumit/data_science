# Plot Pie Chart for Year 2011 Country Wise.

import pandas as pd
import matplotlib as plt

df = pd.read_csv("BigMartSalesData.csv")

df_grouped_country = df.query("Year == 2011").filter(
    ["Country", "Amount"]).groupby(["Country"], as_index=False).sum()

plt.pie(df_grouped_country["Amount"],
        labels=df_grouped_country["Country"],
        autopct='%1.1f%%',
        shadow=True)

plt.tight_layout()
plt.show()

# Which Country contributes highest towards sales?
# United Kingdom
