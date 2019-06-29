from sklearn import metrics
from matplotlib.pylab import rcParams
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Data Collection and reading
data = pd.read_csv("OnlineNewsPopularity.csv")
data.head()


# Analysing data & finding dependent and independent variables
X = data.iloc[:, 1:60]
X.head()

corr = X.corr()
sns.heatmap(corr)
rcParams['figure.figsize'] = 20, 20

Y = data["shares"]
Y.head()


# Splitting data into training and testing
train_x, test_x, train_y, test_y = train_test_split(
    X, Y, random_state=5, test_size=0.20)


# Initializing model and training model
lin_model = LinearRegression()
lin_model.fit(train_x, train_y)

# Predict data
predicted = lin_model.predict(test_x)

# Mean Squared errors
metrics.mean_squared_error(predicted, test_y)

# Plotting predicted and test data
plt.scatter(predicted, test_y)
plt.show()
