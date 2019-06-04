from sklearn import metrics
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 1. Load the kinematics dataset as measured on mobile sensors from the file “run_or_walk.csv”.
# List out the columns in the dataset.
data = pd.read_csv("run_or_walk.csv")
data.head()


# 2. Let the target variable ‘y’ be the activity and assign all the columns after it to ‘x’.
X = data.iloc[:, 5:]
Y = data["activity"]

# 3. Using Scikit-learn fit a Gaussian Naive Bayes model and observe the accuracy.
# Generate a classification report using scikitlearn.
train_x, test_x, train_y, test_y = train_test_split(
    X, Y, random_state=10, test_size=0.30)

g_model = GaussianNB()
g_model.fit(train_x, train_y)

predicted_values = g_model.predict(test_x)

print("\nAccuracy Score\n")
print(metrics.accuracy_score(predicted_values, test_y))

print("\nClassification Score\n")
print(metrics.classification_report(predicted_values, test_y))


# 4.Repeat the model once using only the acceleration values as predictors and then using only the
# gyro values as predictors. Comment on the difference in accuracy between both the models.
# Accelerations as Independent variables
X_A = data.iloc[:, 5:8]
Y_A = data["activity"]

train_x_a, test_x_a, train_y_a, test_y_a = train_test_split(
    X_A, Y_A, random_state=10, test_size=0.30)

g_model.fit(train_x_a, train_y_a)
predicted_values_a = g_model.predict(test_x_a)

print("\nAccuracy Score\n")
print(metrics.accuracy_score(predicted_values_a, test_y_a))

print("\nClassification Score\n")
print(metrics.classification_report(predicted_values_a, test_y_a))


# Gyro as Independent variables
X_G = data.iloc[:, 8:]
Y_G = data["activity"]

train_x_g, test_x_g, train_y_g, test_y_g = train_test_split(
    X_G, Y_G, random_state=10, test_size=0.30)

g_model.fit(train_x_g, train_y_g)
predicted_values_g = g_model.predict(test_x_g)

print("\nAccuracy Score\n")
print(metrics.accuracy_score(predicted_values_g, test_y_g))

print("\nClassification Score\n")
print(metrics.classification_report(predicted_values_g, test_y_g))
