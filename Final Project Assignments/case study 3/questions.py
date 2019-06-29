from sklearn.svm import LinearSVC
from sklearn.naive_bayes import GaussianNB
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn import metrics
from sklearn.model_selection import train_test_split


# Reading training data
train_data = pd.read_csv("train.csv")
train_data.head()

# Reading testing data
test_data = pd.read_csv("test.csv")
test_data.head()


# Encoding Data
labelencoder = LabelEncoder()
train_data["species"] = labelencoder.fit_transform(train_data["species"])
train_data.head()


# Defining dependent and Independent data
X = train_data.iloc[:, 1:]
Y = train_data["species"]


# Train-test data split
train_x, test_x, train_y, test_y = train_test_split(
    X, Y, random_state=5, test_size=20)


# 1. Random Forest Classifier
ran_class = RandomForestClassifier(n_estimators=100)
ran_class.fit(train_x, train_y)

predict_rf = ran_class.predict(test_x)
print("Radom Forest Accuracy Score : ",
      metrics.accuracy_score(predict_rf, test_y))


# 2. Decision Tree Classifier
dec_class = DecisionTreeClassifier()
dec_class.fit(train_x, train_y)

predict_dt = dec_class.predict(test_x)
print("Decision Tree Accuracy Score : ",
      metrics.accuracy_score(predict_dt, test_y))


# 3. Naive Bayes Classifier
gn_class = GaussianNB()
gn_class.fit(train_x, train_y)

predict_gn = gn_class.predict(test_x)
print("Naive Bayes Accuracy Score : ",
      metrics.accuracy_score(predict_gn, test_y))


# 4. SVM Classifier
svm_class = LinearSVC()
svm_class.fit(train_x, train_y)

predict_svm = svm_class.predict(test_x)
print("SVM Accuracy Score : ", metrics.accuracy_score(predict_svm, test_y))


# Best Classifier - Naive Bayes
predict_test = gn_class.predict(test_data)

# labelencoder.inverse_transform(predict_test) : Inverse the encoding
test_data["species"] = labelencoder.inverse_transform(predict_test)
test_data.head()


# save predicted data
test_data.to_csv("Output.csv", index=True)
