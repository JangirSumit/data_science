import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
import seaborn as sns
from sklearn import metrics


# 1.We will use acoustic features to distinguish a male voice from female. Load the dataset from “voice.csv”,
# identify the target variable and do a one-hot encoding for the same. Split the dataset in train-test with 20% 
# of the data kept aside for testing.
# [Hint: Refer to LabelEncoder documentation in scikit-learn]
df_voices = pd.read_csv("voice.csv")
df_voices.head()

df_voices["label"] = df_voices["label"].map({"male":"0", "female":"1"})

X = df_voices.iloc[:,0:19]
Y = df_voices["label"]


# 2.Fit a logistic regression model and measure the accuracy on the test set.
# [Hint:Refer to Linear Models section in scikit-learn]
train_x, test_x, train_y, test_y = train_test_split(X, Y, random_state = 10, test_size = 0.20) 
ln_model = LogisticRegression()
ln_model.fit(train_x, train_y)

predicted_data = ln_model.predict(test_x)

metrics.accuracy_score(predicted_data, test_y)

# 3.Compute the correlation matrix that describes the dependence between all predictors and identify the 
# predictors that are highly correlated.  Plot the correlation matrix using seaborn heatmap.
# [Hint: Explore dataframe methods to identify appropriate method]
corr = df_voices.corr()

sns.heatmap(corr)
plt.show()


# 4.Based on correlation remove those predictors that are correlated and fit a logistic regression model 
# again and compare the accuracy with that of previous model.
# [Hint:Identify correlated variable pairs and remove one among them]

# strong correlated columns So that we can keep
# "meanfreq" -> "median", "Q25", "centroid"
# "Q25" -> "centroid"
# "maxdom" -> "dfrange"

X = X.drop("median",axis=1)
X = X.drop("Q25",axis=1)
X = X.drop("centroid",axis=1)
X = X.drop("dfrange",axis=1)

train_x, test_x, train_y, test_y = train_test_split(X, Y, random_state = 10, test_size = 0.20)

ln_model = LogisticRegression()
ln_model.fit(train_x, train_y)

predicted_data = ln_model.predict(test_x)

metrics.accuracy_score(predicted_data, test_y)