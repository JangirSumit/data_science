from sklearn import metrics
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Data Collection
data = pd.read_csv("loan_borowwer_data.csv")
print(data.head())

# Data Wrangling
X = data.iloc[:, 2:13]
Y = data["not.fully.paid"]

# Split Data
train_x, test_x, train_y, test_y = train_test_split(
    X, Y, random_state=10, test_size=0.3)

# Model creation and Fitting Model
random_class = RandomForestClassifier()
random_class.fit(train_x, train_y)

# Data Prediction
predicted_values = random_class.predict(test_x)

# Check Accuracy Score
metrics.accuracy_score(predicted_values, test_y)
