from sklearn.cluster import AgglomerativeClustering
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import metrics


data = pd.read_csv("zoo.csv")
data.head()

# Find Unique class types
unique_classtypes = np.unique(data["class_type"].values)

# Initialize Agglomerative Clustering
agglo = AgglomerativeClustering(n_clusters=4)
predicted_values = agglo.fit_predict(data.iloc[:, 0:16])

# Accuracy Score
print("Accuracy Score")
print(metrics.accuracy_score(predicted_values, data["class_type"].values))

# Mean Square Error value
print("Mean Squared Error value")
print(metrics.mean_squared_error(predict, data["class_type"].values))
