from sklearn import metrics
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import AdaBoostClassifier
from sklearn.model_selection import train_test_split
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv("letterCG.bin", sep=' ')
data.head()

data.drop(["Unnamed: 5", "Unnamed: 18", "yegvx"], axis=1, inplace=True)
data.fillna(0)

data.head()

X = data.iloc[:, 1:]
Y = data["Class"]

train_x, test_x, train_y, test_y = train_test_split(
    X, Y, random_state=5, test_size=0.30)


base_class = DecisionTreeClassifier(max_depth=1)

ada_Boost = AdaBoostClassifier(
    base_estimator=base_class, n_estimators=400, learning_rate=1, algorithm='SAMME')

ada_Boost.fit(train_x, train_y)
predicted = ada_Boost.predict(test_x)
metrics.accuracy_score(predicted, test_y)

base_class = DecisionTreeClassifier(max_depth=2)
ada_Boost = AdaBoostClassifier(
    base_estimator=base_class, n_estimators=400, learning_rate=1, algorithm='SAMME')

ada_Boost.fit(train_x, train_y)
predicted = ada_Boost.predict(test_x)
metrics.accuracy_score(predicted, test_y)
