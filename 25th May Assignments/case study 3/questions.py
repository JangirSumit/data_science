from math import sqrt
from sklearn.metrics import mean_squared_error
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import seaborn as sns


df_fyntra = pd.read_csv("FyntraCustomerData.csv")
df_fyntra.head()

# 1.Compute --Use seaborn to create a jointplot to compare the Time on Website and Yearly Amount Spent columns.
df_Time_web_Amount = df_fyntra.filter(
    ["Time_on_Website", "Yearly_Amount_Spent"])

sns.set(style="white", color_codes=True)
sns.jointplot(x="Time_on_Website",
              y="Yearly_Amount_Spent", data=df_Time_web_Amount)

# Is there a correlation? : Both have strong correlation
coff_Time_Amount = df_Time_web_Amount.corr()
sns.heatmap(coff_Time_Amount)


# 2.Compute –Do the same as above but now with Time on App and Yearly Amount Spent.
df_Time_app_Amount = df_fyntra.filter(["Time_on_App", "Yearly_Amount_Spent"])

sns.set(style="white", color_codes=True)
sns.jointplot(x="Time_on_App",
              y="Yearly_Amount_Spent", data=df_Time_app_Amount)

# Is there a correlation? : Both have strong correlation
coff_Time_web_Amount = df_Time_app_Amount.corr()
sns.heatmap(coff_Time_web_Amount)


# 3.Compute --Explore types of relationships across the entire data set using pairplot .
sns.set(style="ticks", color_codes=True)
g = sns.pairplot(df_fyntra)

# Based off this plot what looks to be the most correlated feature with Yearly Amount Spent?
X = df_fyntra["Length_of_Membership"]
Y = df_fyntra["Yearly_Amount_Spent"]
train_x, test_x, train_y, test_y = train_test_split(
    X, Y, random_state=85, test_size=0.3)


# 4.Compute –Create linear model plot of Length of Membership and Yearly Amount Spent.
# Does the data fits well in linear plot?
lin_model = LinearRegression()
lin_model.fit(pd.DataFrame(train_x), train_y)

# 5.Compute –Train and Test the data and answer multiple questions --What is the use of random_state=85?
# The random_state splits a randomly selected data but with a twist.
# And the twist is the order of the data will be same for a particular value of random_state.
# You need to understand that it's not a bool accpeted value. starting from 0 to any integer no,
# if you pass as random_state,it'll be a permanent order for it.
# Ex: the order you will get in random_state=0 remain same. After that if you
# execuit random_state=5 and again come back to random_state=0 you'll get the same order.
# And like 0 for all integer will go same. How ever random_state=None splits randomly each time.

# 6.Compute –Predict the data and do a scatter plot. Check if actual and predicted data match?
predicted_values = lin_model.predict(pd.DataFrame(test_x))

plt.scatter(predicted_values, test_y)
plt.show()


# 7.What is the value of Root Mean Squared Error?
rms = sqrt(mean_squared_error(test_y, predicted_values))
print(rms)
