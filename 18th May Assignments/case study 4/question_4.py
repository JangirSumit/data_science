# 4. Plot Scatter Plot for the invoice amounts and see the concentration of amount.
import pandas as pd
import matplotlib as plt

df = pd.read_csv("BigMartSalesData.csv")


invoice_amounts = df.filter(["InvoiceDate", "Amount"]).groupby(
    "InvoiceDate", as_index=False).sum()

plt.scatter(invoice_amounts["InvoiceDate"], invoice_amounts["Amount"])
plt.ylim(20000, 100000)
plt.show()

# In which range most of the invoice amounts are concentrated
# 20000 - 30000
