import pandas as pd
import matplotlib as plt
import numpy as np

df = pd.read_csv("Salaries.csv", low_memory=False)
print(df.head())

# 1. Compute how much total salary cost has increased from year 2011 to 2014
grouped_df = df.groupby(["Year"]).agg("sum").filter(["Year", "TotalPay"])
print(grouped_df.head())

total_pay_2011 = grouped_df.query("Year == 2011")["TotalPay"]
total_pay_2014 = grouped_df.query("Year == 2014")["TotalPay"]

total_change_2011_2014 = float(total_pay_2014) - float(total_pay_2011)

print("Total change from 2011 to 2014 is "+ str(total_change_2011_2014))

#################################################################

# 2. Which Job Title in Year 2014 has highest mean salary?
grouped_df_JobTitle = df.query("Year == 2014").groupby(["JobTitle"]).agg("mean").filter(["JobTitle", "TotalPay"])

max_min_salary = grouped_df_JobTitle[grouped_df_JobTitle["TotalPay"] == grouped_df_JobTitle["TotalPay"].max()]
print("highest mean Salary job title is " + str(max_min_salary))

#################################################################

# 3. How much money could have been saved in Year 2014 by stopping OverTimePay?

grouped_df_overTime = df.groupby(["Year"]).agg("sum").filter(["OvertimePay"]).query("Year == 2014")

print(str(float(grouped_df_overTime["OvertimePay"])) + " money could have been saved in Year 2014 by stopping OverTimePay")

#################################################################

# 4. Which are the top 5 common job in Year 2014 and how much do they cost SFO ?

grouped_df_5_common = df.groupby(["Year", "JobTitle"]).agg("sum").filter(["Year", "TotalPay", "JobTitle"]).query("Year == 2014").sort_values("TotalPay", ascending=False)

print(grouped_df_5_common.head(5))

#################################################################

# 5. Who was the top earning employee across all the years?

grouped_df_5_top_earners = df.groupby(["Year", "TotalPay"]).agg("max").filter(["Year", "TotalPay", "EmployeeName"])

print(grouped_df_5_top_earners.head())