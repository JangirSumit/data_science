import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df_horse = pd.read_csv("horse.csv")
df_horse.head()


# 1.Let’s attempt to predict the survival of a horse based on various observed medical conditions. 
# Load the data from ‘horses.csv’ and observe whether it contains missing values.
# [Hint: Pandas dataframe has a method isnull]
df_horse.isna()


# 2.This dataset contains many categorical features, replace them with label encoding.
# [Hint: Refer to get_dummies methods in pandas dataframe or Label encoder in scikit-learn]
df_horse = pd.get_dummies(df_horse)


# 3.Replace the missing values by the most frequent value in each column.
# [Hint: Refer to Imputer class in Scikit learn preprocessing module]
from sklearn.preprocessing import Imputer
imp = Imputer(missing_values='NaN', strategy='mean', axis=0)
imp = imp.fit(df_horse.iloc[:,1:])
df_horse.iloc[:,1:] = imp.transform(df_horse.iloc[:,1:])


