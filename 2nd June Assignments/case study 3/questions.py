import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn import svm
from sklearn import metrics


data = pd.read_csv("College.csv")
data.head()
