import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


df_cereal = pd.read_csv("FyntraCustomerData.csv")
df_cereal.head()

# 1.Compute --Use seaborn to create a jointplot to compare the Time on Website and Yearly Amount Spent columns.  Is there a correlation?

# 2.Compute –Do the same as above but now with Time on App and Yearly Amount Spent. Is this correlation stronger than 1stOne?

# 3.Compute --Explore types of relationships across the entire data set using pairplot . 
# Based off this plot what looks to be the most correlated feature with Yearly Amount Spent?

# 4.Compute –Create linear model plot of Length of Membership and Yearly Amount Spent. Does the data fits well in linear plot?

# 5.Compute –Train and Test the data and answer multiple questions --What is the use of random_state=85?

# 6.Compute –Predict the data and do a scatter plot. Check if actual and predicted data match?

# 7.What is the value of Root Mean Squared Error?