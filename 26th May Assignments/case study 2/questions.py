from sklearn import metrics
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import Imputer
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

Y = df_horse["outcome"]
X = df_horse.drop(["outcome"], axis=1)

# 2.This dataset contains many categorical features, replace them with label encoding.
# [Hint: Refer to get_dummies methods in pandas dataframe or Label encoder in scikit-learn]
X = pd.get_dummies(X)
X.head()

# 3.Replace the missing values by the most frequent value in each column.
# [Hint: Refer to Imputer class in Scikit learn preprocessing module]
#from sklearn.preprocessing import Imputer
#imp = Imputer(missing_values='NaN', strategy='mean', axis=0)
#imp = imp.fit(df_horse.iloc[:,1:])
#df_horse.iloc[:,1:] = imp.transform(df_horse.iloc[:,1:])

X = X.apply(lambda x: x.fillna(x.value_counts().index[0]))


# 4.Fit a decision tree classifier and observe the accuracy.
dec_tree = DecisionTreeClassifier()
dec_tree.fit(X, Y)
predicted_outcome = dec_tree.predict(X)
metrics.accuracy_score(predicted_outcome, Y)

# 5.Fit a random forest classifier and observe the accuracy
random_forest = RandomForestClassifier()
random_forest.fit(X, Y)
predicted_outcome = random_forest.predict(X)
metrics.accuracy_score(predicted_outcome, Y)
