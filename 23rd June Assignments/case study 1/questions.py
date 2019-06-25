from sklearn import metrics
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split, cross_val_score
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


data = pd.read_csv("bio-degradabale-data.csv", sep=';')
data.head()


data.columns = range(42)
data.head()


X = data.iloc[:, 0:41]
Y = data[41]

train_x, test_x, train_y, test_y = train_test_split(
    X, Y, random_state=5, test_size=.30)


log_model = LogisticRegression()
log_model.fit(train_x, train_y)
predicted = log_model.predict(test_x)

print(metrics.accuracy_score(predicted, test_y))

print(cross_val_score(log_model, X, Y, cv=10, scoring='accuracy').mean())
