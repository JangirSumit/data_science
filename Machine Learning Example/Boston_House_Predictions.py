from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# 1. Data collection

boston_data = pd.read_csv("./BostonHousing.csv")
boston_data.head()


# 2. Data Wrangling

# Input or independent value
X = boston_data.iloc[:, :13]  # selecting columns
# Output or dependent value
Y = boston_data["medv"]


# 3. Data Analysis

corr = boston_data.corr()
sns.heatmap(corr)


# 4. Training the Algorithm


x_train, x_test, y_train, y_test = train_test_split(
    X, Y, test_size=.30, random_state=10)
# model instantiation
linear_model = LinearRegression()
# fit the model with input and corresponding output data
linear_model.fit(x_train, y_train)


# 5. Test Algorithm

predicted_house_price = linear_model.predict(x_test)
plt.scatter(y_test, predicted_house_price)
plt.show()

predicted_dataframe = pd.DataFrame(
    {"Predicted_Prices": predicted_house_price, "Actual_Prices": y_test})
print(predicted_dataframe)
